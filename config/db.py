from pymongo import MongoClient
import os

password = os.environ.get("MONGODB_PWD")

uri = f"mongodb+srv://italo:bhub123@bhub.hpkuayw.mongodb.net/?retryWrites=true&w=majority"
conn = MongoClient(uri)

