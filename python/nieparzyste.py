#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nieparzyste.py

import random




def losuj_nieparzyste(maks):
    nieparzyste = []
    for i in range(200):
        liczby.append(random.randint(0, MAKS_LICZBA)
        if liczba % 2:
            nieparzyste.append(liczba)
    print(len(nieparzyste))


def main(args):
    MAKS_LICZBA = 200
    liczby = []
    suma = 0
    licznik = 0


    for i in range(200):
        liczby.append(random.randint(0, MAKS_LICZBA))
            
    for liczba in range(101):
        if liczba % 2:
            suma = suma + liczba



    print(suma, licznik)


    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
