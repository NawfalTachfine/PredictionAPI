# -*- coding: utf-8 -*-

# Standard Libs
from flask import Flask, request, jsonify

from pandas import DataFrame
from pickle import load
import logging as lg
from datetime import datetime as dt
from pytz import timezone


# Custom Libs
def dummy_encode(in_df, dummies):
    out_df = in_df.copy()

    for feature, values in dummies.items():
        for value in values:
            dummy_name = '{}__{}'.format(feature, value)
            out_df[dummy_name] = (out_df[feature] == value).astype(int)

        del out_df[feature]
    return out_df


def minmax_scale(in_df, boundaries):
    out_df = in_df.copy()

    for feature, (min_val, max_val) in boundaries.items():
        col_name = '{}__norm'.format(feature)

        out_df[col_name] = round((out_df[feature] - min_val)/(max_val - min_val), 3)
        out_df.loc[out_df[col_name] < 0, col_name] = 0
        out_df.loc[out_df[col_name] > 1, col_name] = 1

        del out_df[feature]
        # print('MinMax Scaled feature\t\t{}'.format(feature))
    return out_df
# ******************************************************************************


# Conf
current_time = dt.now(timezone('UTC')).astimezone(timezone('Europe/Paris'))
log_file_name = 'logs/run.{}.log'.format(current_time.strftime("%Y-%m-%d"))

lg.basicConfig(
    filename=log_file_name,
    level=lg.INFO,
    filemode='a',
    format='%(asctime)s\t%(levelname)s\t%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# ******************************************************************************

# Init
app = Flask(__name__)
model = load(open("./pickles/model_v1.pkl", 'rb'))

DUMMIES = {'sex': ['M', 'F', 'I']}

BOUNDARIES = {
    'length': (0.075000, 0.815000),
    'diameter': (0.055000, 0.650000),
    'height': (0.000000, 1.130000),
    'whole_weight': (0.002000, 2.825500),
    'shucked_weight': (0.001000, 1.488000),
    'viscera_weight': (0.000500, 0.760000),
    'shell_weight': (0.001500, 1.005000)
}
# ******************************************************************************

# Core


@app.route('/api/v1.0/aballone', methods=['POST'])
def index():

    # Fetching inputs
    query = request.get_json(silent=True, force=True)['inputs']
    input_df = DataFrame(query)

    # Preparing features
    X_tmp = dummy_encode(input_df, DUMMIES)
    X = minmax_scale(X_tmp, BOUNDARIES)

    # Computing predictions
    y_pred = model.predict(X)
    y_prob = model.predict_proba(X)

    # Building output
    output = [
        {"label": int(y), "prob": round(float(p[0]), 3)}
        for (y, p) in zip(y_pred, y_prob)
    ]

    # Logging predictions
    for (i, o) in zip(query, output):
        lg.info('IN | {} || OUT | {}'.format(i, o))

    return jsonify({'outputs': output})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
