import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['test']
collection = db.students
student1={
    'id':'20170101',
    'name':'zhangsan',
    'age':20,
    'gender':'male'
}
student2={
    'id':'20170102',
    'name':'lisi',
    'age':21,
    'gender':'male'
}
result = collection.insert_many([student1,student2])
# print(result)
# print(result.inserted_ids)

result = collection.find_one({'name':'lisi'})
result = collection.find_one({'_id':ObjectId('5e8aab2b2e246ddbcc3ff0f1')})
print(type(result))
print(result)