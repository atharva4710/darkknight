"""
models.py

Minimal MongoDB connection helpers and placeholder model functions.
"""
import os
from pymongo import MongoClient

def get_mongo_client():
    uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
    return MongoClient(uri)

def get_db(name: str = None):
    client = get_mongo_client()
    dbname = name or os.getenv('MONGO_DBNAME', 'plansphere')
    return client[dbname]

# Example collection accessor
def users_collection():
    return get_db()['users']

# Add your model helpers/classes below
