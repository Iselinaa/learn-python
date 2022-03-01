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

person = { 
    "name": "Marianna",
     "surname": "Lampou"
}

x = table.insert_one(person)

print(x)
