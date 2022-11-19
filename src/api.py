import flask
from flask import Flask, request
import json
from chunkClassifier import classifyChunks
from training import findToxicity

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def negativeBlocks(yt_code):
    data = classifyChunks(yt_code)
    return_data = []
    for i in data:
        if i[2] == "negative" and i[3] >= 0.7:
            return_data.append([i[0], i[1]])
    return return_data

def jsonify(toxicityRating, badTimes):
    data = { "toxicity" : toxicityRating, "badBlocks" : badTimes }
    json_string = json.dumps(data)
    return json_string

@app.route('/s', methods=['GET'])
def home():
    yt_code = request.args.get("yt_code")
    return jsonify(findToxicity(yt_code)[0], negativeBlocks(yt_code))

app.run()