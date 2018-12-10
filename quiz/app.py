#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app route("/strona")
def strona()
    return render_template
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
