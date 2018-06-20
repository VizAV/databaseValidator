from config import path,db
from validateFormat.validateProcess import validateData
from reArrangeFormat.reArrangeProcess import reArrangeData
import pymongo
#initiate DB
print("Connecting to database...")
print()
try:
    conn = pymongo.MongoClient()
    print("Connected successfully!!!")
    print()
except pymongo.errors.ConnectionFailure as e:
    print("Could not connect to MongoDB: %s" % e)
    print()

db = conn[db]

#Validate the datatypes
validatedData = validateData(True)

# Rearrange the data
reArrangedData = reArrangeData(validatedData)

for rows in reArrangedData:
    for keys,values in rows.items():
        if type(values) is not list:
            db[keys].update({"_id": values["ID"]}, {'$set': values}, upsert=True)
        else:
            for info in values:
                db[keys].update({"_id": info["ID"]}, {'$set': info}, upsert=True)


#Push to DB