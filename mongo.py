import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)


coll = conn[DATABASE][COLLECTION]


documents = coll.find({"first": "douglas"})

""" Delete documents with 'first' name set to 'douglas' """
# coll.remove({"first": "douglas"})
# documents = coll.find()

""" Delete whole table """
# coll.remove()


""" Update a single document (first one only) """
# coll.update_one(
#     {"nationality": "american"},
#     {"$set": {"hair_color": "maroon"}}
# )
# documents = coll.find({"nationality": "american"})

""" Update all documents """
# coll.update_many(
#     {"nationality": "american"},
#     {"$set": {"hair_color": "maroon"}}
# )
# documents = coll.find({"nationality": "american"})

# documents = coll.find()

for doc in documents:
    print(doc)
