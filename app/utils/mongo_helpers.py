from pymongo import MongoClient
from app.config import MONGODB_URI, MONGODB_DB_NAME


def get_db():
    """
    Establishes a connection to the MongoDB database and returns the database instance.

    Returns:
        Database: A MongoDB database object for performing operations.
    """
    # Create a MongoClient instance to connect to the MongoDB server.
    # The URI is defined in the configuration file (app.config).
    client = MongoClient(MONGODB_URI)

    # Access the specific database using the database name provided in the configuration.
    db = client[MONGODB_DB_NAME]

    # Return the database instance to the caller for further operations.
    return db
