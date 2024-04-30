import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

class Config:
    password = os.getenv("MONGO_PASSWORD")
    uri = f"mongodb+srv://vehifinder:{password}@vehifinder.rxfuvta.mongodb.net/?retryWrites=true&w=majority&appName=VehiFinder"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['vehifinder']

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)