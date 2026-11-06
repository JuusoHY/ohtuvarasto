"""Varaston yksikkotestit."""

import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Varasto-luokan yksikkotestit."""
    def setUp(self):
        """Alustaa varaston testia varten."""
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Testaa konstruktori luo tyhjan varaston."""
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Testaa uudella varastolla oikea tilavuus."""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Testaa lisays lisaa saldoa."""
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Testaa lisays lisaa pienentaa vapaata tilaa."""
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Testaa ottaminen palauttaa oikean maaran."""
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Testaa ottaminen lisaa tilaa."""
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_liian_suuri_lisays_tayttaa_varaston(self):
        """Testaa liian suuri lisays tayttaa varaston."""
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_liian_suuri_ottaminen_tyhjentaa_varaston(self):
        """Testaa liian suuri ottaminen tyhjentaa varaston."""
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(15)

        self.assertAlmostEqual(saatu_maara, 8)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        """Testaa negatiivinen lisays ei muuta saldoa."""
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_ottaminen_ei_muuta_saldoa(self):
        """Testaa negatiivinen ottaminen ei muuta saldoa."""
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-5)

        self.assertAlmostEqual(saatu_maara, 0)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivinen_alkusaldo_nollataan(self):
        """Testaa negatiivinen alkusaldo nollataan."""
        varasto = Varasto(10, -5)

        self.assertAlmostEqual(varasto.saldo, 0)

    def test_negatiivinen_tilavuus_nollataan(self):
        """Testaa negatiivinen tilavuus nollataan."""
        varasto = Varasto(-10)

        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_liian_suuri_alkusaldo(self):
        """Testaa liian suuri alkusaldo."""
        varasto = Varasto(10, 15)

        self.assertAlmostEqual(varasto.saldo, 10)

    def test_varaston_merkkijonoesitys(self):
        """Testaa varaston merkkijonoesitys."""
        varasto = Varasto(10, 5)

        self.assertEqual(
            str(varasto),
            "saldo = 5, vielä tilaa 5"
        )
