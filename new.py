import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")
db=client['mydata']
collection=db['newdata']
mydict={
    'name':'snesh',
    'age':'23',
    'address':'mtm'
}
x=collection.insert_one(mydict)
print(x)

