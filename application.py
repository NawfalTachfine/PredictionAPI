# -*- coding: utf-8 -*-

# Standard Libs
from flask import Flask
from flask import request
# from flask import render_template
from flask import jsonify

import os
import sys
import numpy as np
import pandas as pd
import sklearn
import pickle as pkl

import json
import requests
import logging as lg
from datetime import datetime as dt
from pytz import timezone

# Custom Libs
sys.path.append("./lib")
sys.path.append("./models")

# ******************************************************************************

# Conf
current_time = dt.now(timezone('UTC')).astimezone(timezone('Europe/Paris'))
log_file_name = 'logs/run.{}.log'.format(current_time.strftime("%Y-%m-%d"))

lg.basicConfig(filename = log_file_name,
               level = lg.INFO,
               filemode = 'a',
               format = '%(asctime)s\t%(levelname)s\t%(message)s',
               datefmt = '%Y-%m-%d %H:%M:%S'
               )

# ******************************************************************************

# Init
app = Flask(__name__)
model = pkl.load(open("/rf.pkl",'r'))

# ******************************************************************************

# Core
@app.route('/api/v1.0/aballone', methods=['POST'])
def index():

    query = request.get_json(silent=True)


    output = {"key":"value"}

    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
