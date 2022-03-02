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

findOne = table.find_one() #find first document
# print(findOne)

# for i in table.find({},{ "_id": 0, "name": 1, "address": 1 }):
  # print(i) #return names and adresses, not ids

myquery1 = { "address": "Park Lane 38" }
mydoc = table.find(myquery1)
# for x in mydoc:
  # print(x)

#find documents where the address starts with 'S'
myquery2 = { "address": { "$regex": "^S" } }
mydoc = table.find(myquery2)
# for x in mydoc:
  # print(x)

#sort the result alphabetically by name
mydoc = table.find().sort("name", 1)
for x in mydoc:
  print(x)

# update all documents where the address starts with the letter 'S':
myquery3 = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }
x = table.update_many(myquery3, newvalues)
print(x.modified_count, "documents updated.")

# limmit the result to 5 douments
myresult = table.find().limit(5)
for x in myresult:
  print(x)

