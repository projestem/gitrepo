#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potegi.py
#
def potega_it(a, n):
    wynik = 1
    
    for i in range(n):
        wynik = wynik * a
    return wynik

def main(args):
    a = int(input("Podaj liczbe: "))
    n = int(input("Podaj wykladnik potegi: "))
    print("Podstawa {} do potęgi {} wynosi {} ". format(a, n, potega_it(a, n)), end='')
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
