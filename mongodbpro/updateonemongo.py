from pymongo import MongoClient
client = MongoClient('localhost',27017)
db=client.result
col=db.biodata
col.update_one({"_id":"4"}, {"$set":{"name":"Joseph"}})