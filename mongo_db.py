from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://sofi-mcc057:sOfIa2006@cluster0.8ndz01r.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.get_database("rate_my_dorm")
dorms = db["dorms"] # create dorm table
tags = db["tags"] # create tags table
reviews = db["reviews"]
overall_ratings = db["overall_ratings"]

def insert_dorm(document):
    dorms.insert_one(document)

def dorms_with_tag(tag):
    dorms.tags.find({"tags" : tag})

def trigger_overall_ratings(dormID):
    dorm_reviews = list(reviews.find({"dormID": dormID}))
    new_review_count = overall_ratings.find({""})