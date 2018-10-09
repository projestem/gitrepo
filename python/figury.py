#!/usr/bin/env python
# -*- coding: utf-8 -*-


def prostokat1(a, b, znak):
    """Drukowanie wypelnionego prostokata"""
    for i in range(i):
        for j in range(j):
            print(z, end='')
        print()


def prostokat2(a, b, znak):
    """Drukowanie wypelnionego prostokata"""
    for i in range(a):
        for j in range(b):
            if i == 0 or i == a-1 or j == 0 or j == b-1:
                print(znak, end='')
            else:
                print(" ", end='')
        print()


def choinka(h, znak):
    for i in range(1, h+1):
        for j in range(i):
            print(znak, end='')
        print()


def choinka2(h, znak):
    for i in range(h):
        for j in range(h-1):
            print(znak, end='')
        print()


def trojkat(h, znak):
    t = (h-1)*2
    for i in range(h-1, -1, -1):
        for j in range(t+1):
            if j < i or j > t-i:
                print(" ", end='')
            else:
                print(znak, end='')
        print()


def main(args):
    # a=int(input("Podaj liczbe wierszy: "))
    # b=int(input("Podaj liczbe kolumn: "))
    h = int(input("Podaj wysokosc choinki: "))
    z = input("Podaj znak: ")

    # h=3
    # z="#"

    # prostokat2(a,b,z)
    #choinka2(h, z)

    trojkat(h, z)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))