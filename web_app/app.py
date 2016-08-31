#!/usr/bin/env python

from lib.deco import calc_deco

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rd_index():
    if request.method == 'POST':
        depth = int(request.form['depth'])
        bottom_time = int(request.form['bottom_time'])
        deco = calc_deco(depth=depth,
                         bottom_time=bottom_time,
                         nosaturation=True)
        return render_template('main.html',
                               deco=deco)
    else:
        return render_template('main.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
