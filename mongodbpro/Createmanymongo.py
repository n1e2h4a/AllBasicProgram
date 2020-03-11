from pymongo import MongoClient
client = MongoClient('localhost',27017)
db=client.result
col=db.biodata
col.insert_many(
   [
     { "city": "Delhi", "salary": "1000"},
     { "city": "mumbai", "salary": "2000"},
     { "city": "Dehradun","salary": "3000"}
   ]
)
