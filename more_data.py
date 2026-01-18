from mongo_db import db

db["overall_ratings"].delete_many({})

for i in range(12):
    db["overall_ratings"].insert_one({
        "overallRating": 5,
        "roomSize": 5,
        "diningProximity": 5,
        "academicProximity": 5,
        "amenities": 5,
        "reviewCount": 0,
        "dormID": i+1
    })