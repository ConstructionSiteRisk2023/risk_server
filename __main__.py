from flask import Flask, request,Response, jsonify, send_file
from flask_cors import CORS, cross_origin
from Modules import Visualizer
import json


app = Flask(__name__, template_folder="templates")
CORS(app, resources={r'*': {'origins': '*'}})

vis = Visualizer("20221118_cid_freq_srs.csv")


@app.route('/params')
def params():
    data = request.json

    vis.select_save_graph(data)
    return send_file(f'Data/temp.jpg', mimetype='image/gif')


@app.route('/predict',methods=['GET','POST'])
def predict():
    data = request.json
    print(data)
    return Response(json.dumps({"result" : 12}))


if __name__ == "__main__":
    app.run(host="localhost", port = 4000)