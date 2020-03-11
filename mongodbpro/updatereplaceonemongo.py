from pymongo import MongoClient
client = MongoClient('localhost',27017)
db=client.result
col=db.biodata
col.replace({"name":"niharika"} ,{"name":"neharika"})