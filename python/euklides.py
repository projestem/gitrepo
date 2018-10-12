#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  euklides.py
#  
#  Copyright 2018  <>
#  


def euklides(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return(a)
    
def nww(a, b):
    
    
def main(args):
    
    a = int(input("Podaj liczbe: "))
    b = int(input("Podaj liczbe: "))
    print (euklides(a, b))
    
    return 0
    
if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
