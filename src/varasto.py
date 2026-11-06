"""Yksinkertainen varastosovellus."""


class Varasto:
    """Kuvaa varastoa, jolla on enimmäistilavuus ja saldo."""

    def __init__(self, tilavuus, alku_saldo=0):
        """Alustaa varaston kelvollisilla arvoilla."""
        self.tilavuus = max(0.0, tilavuus)
        self.saldo = max(0.0, min(alku_saldo, self.tilavuus))

    def paljonko_mahtuu(self):
        """Palauttaa varastossa vapaan tilan."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Lisaa varastoon maaran sallituissa rajoissa."""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Ottaa varastosta toteutuvan maaran."""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0
            return kaikki_mita_voidaan
        self.saldo = self.saldo - maara
        return maara

    def __str__(self):
        """Palauttaa varaston tilan tekstina."""
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"


# Git pull harjoitus
