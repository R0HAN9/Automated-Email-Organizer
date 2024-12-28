from pymongo import MongoClient
from app.config import MONGODB_URI, MONGODB_DB_NAME


def get_db():
    client = MongoClient(MONGODB_URI)
    db = client[MONGODB_DB_NAME]
    return db
