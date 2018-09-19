#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
#  

def trojkat(a, b, c):
    """
    Funkcja bada mozliwosc zbudowania trojkata z trzech podanych bokow
    Funkcja zwraca True jezeli sie dam False w przeciwnym wypadku
"""
    if a + b > c and b + c > a and a + c > b:
        return True
    
    return False

    
def main(args):
    assert(trojkat(3, 4, 1) == True)
    assert(trojkat(3, 4, 1) == False)
    

    
    if trojkat(a, b, c):
        print("Da się")
    else:
        print("Ni hy hy")
            
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
