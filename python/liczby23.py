#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby2-3.py
# 


def liczby2(a=10, b=99):
    
    for liczba in range(10, 99):
        if (liczba % 11) != 0:
            print(liczba)
        print()
			          


def main(args):
    
    print(liczby2())
    
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
