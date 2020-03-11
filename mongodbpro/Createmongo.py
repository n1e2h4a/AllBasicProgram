from pymongo import MongoClient
client = MongoClient('localhost',27017)
db=client.result
col=db.biodata
col.insert(
   {
      "phone":"234566",
      "city":"delhi",
   }
)
