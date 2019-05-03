from random import randrange
import util

def tah_pocitace(pole):

    symbol = "o"
    opakovani = 1
    while True:
        cislo_policka = randrange(20)
        if pole[cislo_policka] == "-":
            return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
        opakovani +=1
