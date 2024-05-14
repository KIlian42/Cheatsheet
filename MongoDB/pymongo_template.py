import pymongo
from pymongo import MongoClient

def main():
    cluster = MongoClient("")
    db = cluster["test"]
    collection = db["products"]

    collection.insert_one({"_id": 123})


if __name__ == "__main__":
    main()