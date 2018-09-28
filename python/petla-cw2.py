#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla-cw2.py
#

def main(args):
    
    start = int(input("Przedział lewy: "))
    stop = int(input("Przedział prawy: "))
    
    for liczba in range(start, stop + 1):
        print(liczba, " ", end ='')
    
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
