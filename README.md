##Hashmapper

Simple flask server that hits the Twitter streaming API at /statuses/:filter looking for particular queries configured through yaml, and then saves them to some MongoDB instance. Very WIP, not completely configurable yet.

####Configuration

Hashmapper has two main config files, *config/db.yaml* and *config/search.yaml*. 

*db.yaml*
	
	name: [name of the database table you'll be using]
	uri: [full mongo uri in the form mongodb://[user]:[pass]@[db_hostname]:port]
	consumer_key: [twitter application consumer key]
	consumer_secret: [twitter application consumer secret]
	access_token_key: [twitter application access token key]
	access_token_secret: [twitter application access token secret]

*search.yaml*

	queries: [double quote enclosed, comma separated string of search terms]

Multiple queries in search.yaml will be treated as A OR B OR C for search purposes. *search.yaml* will be populated with more configuration info in later updates.

####Data Model

Hashmapper's default data model is 

    obj = {
	    "text": item['text'],
	    "created_at": item["created_at"],
	    "geo": item["geo"],
	    "place": item["place"],
	    "coordinates": item["coordinates"],
	    "user": item["user"],
	    "keywords": query
    }

where item is a single tweet as returned by the streaming API.

####Running Hashmapper

First create a Twitter application at https://dev.twitter.com and register the user and access keys. Then set up an instance of MongoDB, either locally or as part of a remote application. Populate config/db.yaml and config/search.yaml with the relevant information.

To run the server:

	$ sudo pip install -r requirements.txt
	$ python server.py

