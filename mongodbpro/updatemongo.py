from pymongo import MongoClient
client = MongoClient('localhost',27017)
db=client.result
col=db.biodata
col.update_many({"_id":"4"}, {"$set":{"height":"5"}})
