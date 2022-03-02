from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

DATABASE_USER = "user"
DATABASE_PASSWORD = "pswdu1s2e3r4"
DABASE_CONNECTION_STRING = f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASSWORD}@test.efbx8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"


# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(DABASE_CONNECTION_STRING, tls=True, tlsAllowInvalidCertificates=True)

db=client.test
table = db["people"]

person = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"}
]

# x = table.insert_many(person)

# print(x.inserted_ids) #print list of the id values of the inserted documents

findOne = table.find_one() #find first document
# print(findOne)

# for i in table.find({},{ "_id": 0, "name": 1, "address": 1 }):
  # print(i) #return names and adresses, not ids

myquery = { "address": "Park Lane 38" }
mydoc = table.find(myquery)
for a in mydoc:
  print(a)

# x = table.delete_many({})
# print(x.deleted_count, " documents deleted.")