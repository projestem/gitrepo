#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  views.py
#  

from flask import Flask, g
from flask import render_template, request
from model_orm import *

app = Flask(__name__)

#widom domyslny
@app.route("/")
def hello():
    return "<h1>Witaj na serwerze!</h1><h2>Aplikacja quiz</h2>"
    
@app.route("/quiz") #definicja zasobu
def quiz():
    pytania = Pytanie.select()
    return render_template('quiz.html', query = pytania)
    
@app.route("/klasa")
def klasa():
    return render_template('klasa.html')

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
