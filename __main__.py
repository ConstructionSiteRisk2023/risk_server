from flask import Flask, request, jsonify, send_file
from Modules import Visualizer
import json


app = Flask(__name__, template_folder="templates")

vis = Visualizer("20221118_cid_freq_srs.csv")


@app.route('/params')
def params():
    data = request.json

    vis.select_save_graph(data)
    return send_file(f'Data/temp.jpg', mimetype='image/gif')


@app.route('/predict')
def predict():
    data = request.json
    return str('0')


if __name__ == "__main__":
    app.run(host="localhost", port = 4000)