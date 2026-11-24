"""Flask-verkkokayttoliittyma varastojen hallintaan."""

import math
import secrets

from flask import (
    Blueprint,
    Flask,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from .varasto import Varasto

web = Blueprint("web", __name__)


def _warehouses():
    return current_app.config["WAREHOUSES"]


def _selected_warehouse():
    """Palauttaa lomakkeessa valitun varaston tai nayttaa virheen."""
    try:
        warehouse_index = int(request.form.get("warehouse", ""))
    except ValueError:
        flash("Valitse kelvollinen varasto.", "error")
        return None

    warehouses = _warehouses()
    if warehouse_index < 0 or warehouse_index >= len(warehouses):
        flash("Valitse kelvollinen varasto.", "error")
        return None
    return warehouses[warehouse_index]


def _positive_number(field, description):
    """Lukee lomakkeesta positiivisen, äärellisen luvun."""
    try:
        number = float(request.form.get(field, ""))
    except ValueError:
        flash(f"{description} on annettava positiivisena lukuna.", "error")
        return None

    if not math.isfinite(number) or number <= 0:
        flash(f"{description} on annettava positiivisena lukuna.", "error")
        return None
    return number


def _warehouse_name():
    name = request.form.get("name", "").strip()
    if not name:
        flash("Varaston nimi ei saa olla tyhjä.", "error")
    return name


def _store_warehouse(name, capacity):
    _warehouses().append({"name": name, "storage": Varasto(capacity)})
    flash(f"Varasto {name} luotiin.", "success")


def _add_to_storage(warehouse, amount):
    storage = warehouse["storage"]
    previous_balance = storage.saldo
    storage.lisaa_varastoon(amount)
    added = storage.saldo - previous_balance
    if added < amount:
        flash(f"Varasto tuli täyteen. Lisättiin {added:g} yksikköä.", "success")
    else:
        flash(f"Varastoon lisättiin {added:g} yksikköä.", "success")


@web.get("/")
def index():
    """Näyttää varastoluettelon ja lomakkeet."""
    return render_template("index.html", warehouses=_warehouses())


@web.post("/warehouses")
def create_warehouse():
    """Luo varaston lomakkeen tiedoilla."""
    name = _warehouse_name()
    capacity = _positive_number("capacity", "Tilavuus")
    if not name or capacity is None:
        return redirect(url_for("web.index"))

    _store_warehouse(name, capacity)
    return redirect(url_for("web.index"))


@web.post("/add")
def add_to_warehouse():
    """Lisää tavaraa valittuun varastoon."""
    warehouse = _selected_warehouse()
    amount = _positive_number("amount", "Määrä")
    if warehouse is None or amount is None:
        return redirect(url_for("web.index"))

    _add_to_storage(warehouse, amount)
    return redirect(url_for("web.index"))


@web.post("/remove")
def remove_from_warehouse():
    """Ottaa tavaraa valitusta varastosta."""
    warehouse = _selected_warehouse()
    amount = _positive_number("amount", "Määrä")
    if warehouse is None or amount is None:
        return redirect(url_for("web.index"))

    removed = warehouse["storage"].ota_varastosta(amount)
    if removed < amount:
        flash(
            f"Varastosta otettiin {removed:g} yksikköä. Varasto tyhjeni.",
            "success",
        )
    else:
        flash(f"Varastosta otettiin {removed:g} yksikköä.", "success")
    return redirect(url_for("web.index"))


def create_app():
    """Luo sovelluksen ja sen muistissa sailyvan varastolistan."""
    application = Flask(__name__)
    application.secret_key = secrets.token_hex(16)
    application.config["WAREHOUSES"] = []
    application.register_blueprint(web)
    return application


app = create_app()
