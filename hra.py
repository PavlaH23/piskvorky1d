from piskvorky import tah_hrace, vyhodnot
from ai import tah_pocitace


pole = "-" * 20
na_tahu = "x"

while True:
    if na_tahu == "x":
        cislo_policka = int(input("""Zadej pozici od 0 do 19: """))
        pole = tah_hrace(pole)
        na_tahu = "o"
    elif na_tahu == "o":
        pole = tah_pocitace(pole)
        na_tahu = "x"

    vysledek = vyhodnot(pole)
    print(pole)

    if vysledek != "-":
        if vysledek == "!":
            print("Remiza! {}".format(pole))
        elif vysledek == "x":
            print("Vyhravas nad pocitacem! {}".format(pole))
        elif vysledek == "o":
            print("Bohuzel, pocitac vyhral. {}".format(pole))
        else:
            raise ValueError("Nepripustny vysledek hry '{}'".format(vysledek))
        break

