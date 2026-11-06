"""Varasto-luokan toiminnan esittely."""

from varasto import Varasto


def nayta_alkutilanne(mehua, olutta):
    """Tulostaa alkuarvot."""
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")


def nayta_getterit(olutta):
    """Tulostaa olutvaraston tiedot."""
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def kokeile_mehuvarastoa(mehua):
    """Kokeilee varastoon lisaamista ja ottamista."""
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def kokeile_virheellisia_varastoja():
    """Kokeilee virheellisia alkuarvoja."""
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)
    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def kokeile_suurta_lisaysta(olutta, mehua):
    """Kokeilee suuria ja negatiivisia lisayksia."""
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")


def kokeile_oluen_ottamista(olutta):
    """Kokeilee liian suurta ottamista."""
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")


def kokeile_mehun_ottamista(mehua):
    """Kokeilee negatiivisen maaran ottamista."""
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def main():
    """Suorittaa Varasto-luokan kokeilut."""
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    nayta_alkutilanne(mehua, olutta)
    nayta_getterit(olutta)
    kokeile_mehuvarastoa(mehua)
    kokeile_virheellisia_varastoja()
    kokeile_suurta_lisaysta(olutta, mehua)
    kokeile_oluen_ottamista(olutta)
    kokeile_mehun_ottamista(mehua)


if __name__ == "__main__":
    main()
