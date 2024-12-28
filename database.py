from pymongo import MongoClient
from os import environ
from dotenv import load_dotenv



def db_conn():
    load_dotenv()
    mongo_uri = environ.get('MONGODB_URI')
    database_name = environ.get('DATABASE_NAME')
    try:
        client = MongoClient(mongo_uri)
        database_connection = client[database_name]
        return database_connection
    except Exception as error:
        return False
    

