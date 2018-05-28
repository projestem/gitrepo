#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    liczba = random.randint(1, 10)  # losowanie liczby
    # print("Wylosowano:", liczba)
    # pobieranie danych od uzytkownika
    for i in range(3):
        print("Próba", i + 1)
        odp = input("Podaj liczba od 1 do 10: ")  # losowanie liczby
        print("Podałeś:", odp)

        if liczba == int(odp):  # porownanie odp z wylosowana liczba
            print("Zgadłeś!")
            break  # przerwanie dzialania petli
        elif i == 2:
            print("Wylosowano:", liczba)
        else:
            print("Spróbuj innym razem!")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
