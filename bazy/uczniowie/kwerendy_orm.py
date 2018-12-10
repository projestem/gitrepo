#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy_orm.py
 
from model_orm import *
 
def kw01():
    #query = Uczen.select().order_by(Uczen.nazwisko.asc())
    #query = Uczen.select().where(Uczen.imie.startswith('G'))
    #query = Uczen.select().where(Uczen.imie.endswith('a'))
    #query = Uczen.select().where(Uczen.imie == 'Rafał')
    #query = Uczen.select().where(Uczen.egz_mat > 40)
    query = Uczen.select().where(Uczen.egz_mat.between(30, 35))
    for obj in query:
        print(obj.nazwisko, obj.imie)
 
def kw02():
    query = (Uczen
        .select(Uczen.nazwisko, Uczen.imie, Uczen.klasa.nazwa)
        .join(Klasa)
    )
    for obj in query:
        print(obj.nazwisko, obj.imie, obj.klasa.nazwa)
 
 
def kw03():
    query = (Ocena
        .select(Ocena.uczen.nazwisko, fn.COUNT(Ocena.ocena).alias('ile_ocen'))
        .join(Uczen)
        .group_by(Ocena.uczen.nazwisko)
    )
    for obj in query:
        print(obj.uczen.nazwisko, obj.ile_ocen)

def kw05():
    query = (Ocena
    .
        
 
def main(args):
    baza.connect()
    
    #kw01()
    #kw02()
    #kw03()
    #kw04
    kw05
    return 0
 
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
