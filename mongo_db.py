from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import math

uri = "mongodb+srv://sofi-mcc057:sOfIa2006@cluster0.8ndz01r.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.get_database("rate_my_dorm")
dorms = db["dorms"] # create dorm table
tags = db["tags"] # create tags table
reviews = db["reviews"]
users = db["users"]
overall_ratings = db["overall_ratings"]

def insert_dorm(document):
    dorms.insert_one(document)

def dorms_with_tag(tag):
    dorms.tags.find({"tags" : tag})

# def trigger_overall_ratings(dormID):
#     dorm_reviews = list(reviews.find({"dormID": dormID}))
#     new_review_count = overall_ratings.find({""})

def trigger_overall_ratings(dormID):
    dorm_reviews = list(reviews.find({"dormID": dormID}))
    review_count = len(dorm_reviews)

    if review_count == 0:
        print(f"No reviews found for dormID {dormID}")
        return

    total_room = 0
    total_dining = 0
    total_academic = 0
    total_amenities = 0

    for r in dorm_reviews:
        total_room += r.get("roomSize", 0)
        total_dining += r.get("diningProximity", 0)
        total_academic += r.get("academicProximity", 0)
        total_amenities += r.get("amenities", 0)

    avg_room = math.ceil(total_room / review_count)
    avg_dining = math.ceil(total_dining / review_count)
    avg_academic = math.ceil(total_academic / review_count)
    avg_amenities = math.ceil(total_amenities / review_count)
    overall_rating = math.ceil((avg_room + avg_dining + avg_academic + avg_amenities) / 4)

    overall_ratings.update_one(
        {"dormID": dormID},
        {
            "$set": {
                "reviewCount": review_count,
                "roomSize": avg_room,
                "diningProximity": avg_dining,
                "academicProximity": avg_academic,
                "amenities": avg_amenities,
                "overallRating": overall_rating
            }
        },
        upsert=True
    )