from flask import render_template, jsonify
import models
import code

def index():
    return render_template('index.html')

def tweets():
    tweets = []
    for t in models.Tweet.find():
        tweets.insert(0, {"location": t["place"]["bounding_box"]["coordinates"][0][0], "text":t["text"]})
    return jsonify({"tweets": tweets})