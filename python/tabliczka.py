#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tabliczka.py
#
def tabliczka():
    a = int(input("Podaj zakres liczb w kolumnie: "))
    b = int(input("Podaj zakres liczb w wierszu: "))
    
    for kolumna in range(1, a + 1): #pętla zewnętrzna
        for wiersz in range(1, b + 1): #pętla wewnętrzna
            print("{:>3} ".format(wiersz*kolumna), end='')
        print()

def main(args):
    tabliczka()
    
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
