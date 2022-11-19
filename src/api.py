import flask
from flask import Flask, request
import json
from training import findToxicity

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def jsonify(toxicityRating):
    data = { "toxicity" : toxicityRating }
    json_string = json.dumps(data)
    return json_string

@app.route('/s', methods=['GET'])
def home():
    yt_code = request.args.get("yt_code")
    return jsonify(findToxicity(yt_code))

app.run()