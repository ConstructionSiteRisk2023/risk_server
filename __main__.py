from flask import Flask, request, jsonify, send_file
from Modules import Visualizer
import json


app = Flask(__name__, template_folder="templates")

vis = Visualizer("20221118_cid_freq_srs.csv")

@app.route('/params')
def params():
    data = request.json
    # data = jsonify(data)
    xparam = data.pop("value_count")
    print(xparam)
    result = vis.select_data(data)
    # print(result)
    # print(len(result))
    vis.save_graph(result,xparam)
    return send_file(f'Data/temp.jpg', mimetype='image/gif')
    # return data


if __name__ == "__main__":
    app.run(host="localhost", port = 4000)