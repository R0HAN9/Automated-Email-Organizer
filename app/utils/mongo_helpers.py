# mongo_helper.py
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from app.config import MONGODB_URI, MONGODB_DB_NAME


def get_db():
    """Get MongoDB database connection"""
    try:
        client = MongoClient(MONGODB_URI)
        # Test the connection
        client.admin.command('ping')
        db = client[MONGODB_DB_NAME]
        return db
    except ConnectionFailure as e:
        print(f"Failed to connect to MongoDB: {e}")
        return None


def save_emails_to_db(emails, collection_name="emails"):
    """Save emails to MongoDB"""
    try:
        db = get_db()
        if db is not None:
            collection = db[collection_name]
            if isinstance(emails, list):
                result = collection.insert_many(emails)
                return result.inserted_ids
            else:
                result = collection.insert_one(emails)
                return result.inserted_id
    except Exception as e:
        print(f"Error saving emails to database: {e}")
        return None
