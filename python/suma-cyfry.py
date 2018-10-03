#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma-cyfry.py
#  
#sumuje cyfry podanej liczby(minimum dwucyfrowej i wyswietla ich sume w terminalu)


def main(args):
    liczba = input("Podaj liczbę 2-cyfrowa: ")
    liczba = int(liczba)
    
    while liczba < 10:
        a = input("Podaj liczbę 2-cyfrowa: ")
        liczba = int(liczba)
        
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba = int(liczba / 10)
        
    print("Suma:", sumuj_cyfry1(liczba))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
