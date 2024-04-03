from pymongo.mongo_client import MongoClient
import os
from pymongo.server_api import ServerApi
from dotenv import load_dotenv


load_dotenv()


def connect_to_database():
    URI = os.getenv("URI")

    client = MongoClient(URI, server_api=ServerApi('1'))
    db = client.get_database()

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        return None, None
    return client, db 
    

# Call the function to establish a connection to the database
client, db = connect_to_database()

if client and db:
    print("Connection successful!")
else:
    print("Connection failed. Exiting...")
    exit(1)  # Exit script if connection failed


