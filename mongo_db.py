from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://sofi-mcc057:sOfIa2006@cluster0.8ndz01r.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.get_database("rate_my_dorm")
dorms = db["dorms"] # create dorm table
tags = db["tags"] # create tags table