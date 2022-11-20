import flask
from flask import Flask, request
import json
from chunkClassifier import classifyChunks
from training import findToxicity
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
cors = CORS(app, resources={r'/*' : {'origins': ['http://localhost:3000']}})
app.config['CORS_HEADERS'] = 'Content-Type'


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

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', 'localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')

@app.route('/s', methods=['GET'])
@cross_origin()
def home():
    yt_code = request.args.get("yt_code")
    resp = flask.jsonify({findToxicity(yt_code)[0]: negativeBlocks(yt_code)})
    # resp.headers.add("Access-Control-Allow-Origin", "chrome-extension://oeockeilbijfieolfdibjfjalgbamdoe")
    print(resp)
    return resp

app.run()