from flask import Blueprint, request
from handlers import main_handler
import models
import code
from flask import Flask, current_app
from flask.ext.pymongo import PyMongo, ObjectId
from TwitterAPI import TwitterAPI
import threading
import yaml

db = yaml.load(open("config/db.yaml"))

app = Flask(__name__)
app.config['MONGO_DBNAME'] = db["name"]
app.config['MONGO_URI'] = db["uri"]

mongo = PyMongo(app)

with app.app_context():
    models.Tweet.initialize_db(mongo.db.tweets)

api = TwitterAPI(db["consumer_key"], db["consumer_secret"],
    db["access_token_key"], db["access_token_secret"])

if __name__ == '__main__':
    boundbox = ",".join(db["twitter_boundbox"].split(" "))
    query = db["twitter_query"].split()
    print ("bounding box of %s, querying %s" % (boundbox, query))    
    t = threading.Thread(target=models.Tweet.start_stream, args=(api, boundbox, query, ))
    t.start()
    
    app.run()


@app.route("/")
def main_page():
    return main_handler.index()

@app.route("/tweets")
def tweets():
    return main_handler.tweets()