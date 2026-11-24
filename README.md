# ohtuvarasto
[![CI](https://github.com/JuusoHY/ohtuvarasto/actions/workflows/main.yml/badge.svg)](https://github.com/JuusoHY/ohtuvarasto/actions)
[![codecov](https://codecov.io/gh/JuusoHY/ohtuvarasto/graph/badge.svg?token=KPTFOYQSCW)](https://codecov.io/gh/JuusoHY/ohtuvarasto)

## Verkkosovellus

Asenna projektin riippuvuudet:

```sh
uv sync
```

Käynnistä Flask-sovellus projektin juurihakemistosta:

```sh
uv run python -m flask --app src.app run
```

Avaa sovellus osoitteessa <http://127.0.0.1:5000>. Varastot säilyvät muistissa
niin kauan kuin sovellusprosessi on käynnissä.

Suorita verkkosovelluksen ja Varasto-luokan testit projektin juurihakemistosta:

```sh
uv run python -m pytest
```
