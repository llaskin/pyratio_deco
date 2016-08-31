#!/usr/bin/env python

from rdlib.deco import calc_deco

from flask import Flask
from flask import request
from flask import render_template
from flask import json


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


@app.route('/api', methods=['GET', 'POST'])
def rd_rest():
  if request.method == 'POST':
      error = {"error": "invalid method"}
      data = json.dumps(request.json)
      if 'depth' and 'bottom_time' in data:
          data = json.loads(data)
          depth = int(data['depth'])
          bottom_time = int(data['bottom_time'])
          deco = calc_deco(depth=depth,
                     bottom_time=bottom_time,
                     nosaturation=True)
          return json.dumps(deco, indent=4)
      else:
          return json.dumps(error)
  else:
      return json.dumps(error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
