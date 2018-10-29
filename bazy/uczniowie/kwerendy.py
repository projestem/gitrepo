#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
#  
import sqlite3

def kwerenda(cur):
    cur.execute("""
        SELECT imie, nazwiko, AVG(ocene) AS pole FROM uczniowie JOIN oceny ON 
    """)

def main(args):
    # KONFIGURACJA ######
    baza_nazwa = 'baza'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    roz = '.csv'
    #####################
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
