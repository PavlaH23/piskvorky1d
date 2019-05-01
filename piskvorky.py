def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]

def tah_hrace(pole):
    while True:
        symbol = "x"
        cislo_policka = int(input("""Zadej pozici od 0 do 19: """))
        if cislo_policka < 0 or cislo_policka > 19:
            print("Zadali jste spatne cislo. Zadejte cislo od 0 do 19.")
        elif pole[cislo_policka] != "-":
            print("Policko je jiz obsazene. Zkus to znova.")
        else:
            return tah(pole, cislo_policka, symbol)

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"
