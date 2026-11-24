"""Verkkokayttoliittyman testit."""

import pytest

from src.app import create_app


@pytest.fixture(name="client")
def make_client():
    """Luo jokaiselle testille tyhjän sovelluksen ja testiasiakkaan."""
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def create_warehouse(client, name, capacity):
    """Luo varaston testiasiakkaalla."""
    return client.post(
        "/warehouses",
        data={"name": name, "capacity": str(capacity)},
        follow_redirects=True,
    )


def test_warehouses_can_be_created_and_listed(client):
    """Luodut varastot näkyvät nimineen ja arvoineen."""
    create_warehouse(client, "Mehu", 10)
    response = create_warehouse(client, "Olut", 20)

    assert b"Mehu" in response.data
    assert b"Olut" in response.data
    assert b">10.0<" in response.data
    assert b">20.0<" in response.data
    assert response.data.count(b">0.0<") == 2


@pytest.mark.parametrize(
    ("name", "capacity"),
    [("", "10"), ("   ", "10"), ("Varasto", "0"), ("Varasto", "-1"),
     ("Varasto", "abc"), ("Varasto", "nan"), ("Varasto", "inf")],
)
def test_invalid_warehouse_is_not_created(client, name, capacity):
    """Virheelliset nimet ja tilavuudet eivät luo varastoa."""
    response = create_warehouse(client, name, capacity)

    assert b"error" in response.data
    assert b"Varastoja ei ole viel" in response.data


def test_add_and_remove_update_the_selected_warehouse(client):
    """Tavaraa lisätään ja otetaan valitusta varastosta."""
    create_warehouse(client, "First", 10)
    create_warehouse(client, "Second", 5)

    client.post(
        "/add",
        data={"warehouse": "1", "amount": "3"},
        follow_redirects=True,
    )
    response = client.post(
        "/remove",
        data={"warehouse": "1", "amount": "2"},
        follow_redirects=True,
    )

    assert b"First" in response.data
    assert b"Second" in response.data
    assert b">1.0<" in response.data
    assert b">10.0<" in response.data


def test_adding_more_than_capacity_does_not_exceed_it(client):
    """Varasto-luokka rajoittaa saldon enimmäistilavuuteen."""
    create_warehouse(client, "Pieni", 5)

    response = client.post(
        "/add",
        data={"warehouse": "0", "amount": "8"},
        follow_redirects=True,
    )

    assert b">5.0<" in response.data
    assert b"Varasto tuli t" in response.data


@pytest.mark.parametrize("amount", ["", "abc", "0", "-2", "nan", "inf"])
def test_invalid_amount_is_reported_without_changing_balance(client, amount):
    """Virheellinen määrä ei muuta saldoa."""
    create_warehouse(client, "Testi", 5)

    response = client.post(
        "/add",
        data={"warehouse": "0", "amount": amount},
        follow_redirects=True,
    )

    assert b"error" in response.data
    assert b">0.0<" in response.data


def test_invalid_warehouse_selection_is_reported(client):
    """Virheellinen varastovalinta ilmoitetaan käyttäjälle."""
    create_warehouse(client, "Testi", 5)

    response = client.post(
        "/remove",
        data={"warehouse": "4", "amount": "2"},
        follow_redirects=True,
    )

    assert b"Valitse kelvollinen varasto." in response.data
    assert b">0.0<" in response.data
