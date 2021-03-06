class Model(object):
    dbMap = None

    @staticmethod
    def initialize_db(conn):
        Model.dbMap = conn

    @staticmethod
    def find_one(query={}):
        return Model.dbMap.find_one(query)

    @staticmethod
    def find(query={}, limit=0):
        # processing here
        return Model.dbMap.find(query).limit(limit)

    @staticmethod
    def insert(obj):
        # needs validation probably
        return Model.dbMap.insert(obj)

    @staticmethod
    def count():
        return Model.dbMap.count()

    @staticmethod
    def delete(query={}):
        return Model.dbMap.remove(query)

class Tweet(Model):
    
    MAX_NUM = 10000

    @staticmethod
    def start_stream(api, hashtags):
        try:
            r = api.request('statuses/filter', {'track': hashtags})
            for item in r:
                obj = {
                "text": item['text'],
                "created_at": item["created_at"],
                "geo": item["geo"],
                "place": item["place"],
                "coordinates": item["coordinates"],
                "user": item["user"],
                "keywords": hashtags
                }
                if Tweet.count() < Tweet.MAX_NUM:
                    Tweet.insert(obj)
                else:
                    Tweet.delete(Tweet.find().sort({"_id":1}).limit(1))
                    Tweet.insert(obj)
        except ProtocolError:
            print "Encountered a connection error, incomplete read."
        finally:
            Tweet.start_stream(api, hashtags)