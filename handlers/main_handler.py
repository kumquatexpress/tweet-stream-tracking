from flask import render_template, jsonify
import models
import code

def index():
    return render_template('index.html')

def tweets():
    results = models.Tweet.find()
    return jsonify(**results)