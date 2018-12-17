#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py

from flask import Flask, g
from flask import render_template, request
from model_orm import *

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = baza
    g.db.connect()
    
@app.after_request
def after_request(response):
    g.db.close()
    return response




if __name__ == '__main__':
app.run(debug=True)
