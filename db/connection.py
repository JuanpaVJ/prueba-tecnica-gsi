from pymongo import MongoClient
import os

mongo_url = os.getenv("MONGO_URL", "mongodb://db:27017")
db = os.getenv("DATABASE_NAME", "task_manager")

client = MongoClient(mongo_url)
db = client[db]
