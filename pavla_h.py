import random


def tah_pocitace(pole, symbol):
    opakovani = 1
    while True:
        cislo_policka = random.randrange(20)
        if pole[cislo_policka] == "-":
            return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
        opakovani +=1
