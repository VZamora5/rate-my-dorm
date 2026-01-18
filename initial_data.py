from mongo_db import db

db["dorms"].delete_many({})
db["reviews"].delete_many({})
db["overall_ratings"].delete_many({})
db["users"].delete_many({})

buildings = [
    {
        "name": "Daniels Hall",
        "dormID": 1,
        "address": "101 Institute Rd",
        "rating": 0,
        "tags": ["first-year", "communal bathroom", "triples"]
    },
    {
        "name": "East Hall",
        "dormID": 2,
        "address": "102 Institute Rd",
        "rating": 0,
        "tags": ["upperclass", "private bathroom", "suite-style", "singles", "doubles", "laundry room", "kitchen"]
    },
    {
        "name": "Faraday Hall",
        "dormID": 3,
        "address": "103 Institute Rd",
        "rating": 0,
        "tags": ["upperclass", "private bathroom", "suite-style", "singles", "doubles", "laundry room", "kitchen"]
    },
    {
        "name": "Founders Hall",
        "dormID": 4,
        "address": "104 Institute Rd",
        "rating": 0,
        "tags": ["first-year", "private bathroom", "suite-style", "singles", "doubles", "triples", "laundry room"]
    },
    {
        "name": "Institute Hall",
        "dormID": 5,
        "address": "105 Institute Rd",
        "rating": 0,
        "tags": ["first-year", "communal bathroom", "singles", "doubles", "triples", "laundry room"]
    },
    {
        "name": "Messenger Hall",
        "dormID": 6,
        "address": "106 Institute Rd",
        "rating": 0,
        "tags": ["first-year", "communal bathroom", "singles", "doubles", "laundry room"]
    },
    {
        "name": "Morgan Hall",
        "dormID": 7,
        "address": "107 Institute Rd",
        "rating": 0,
        "tags": ["first-year", "communal bathroom", "triples", "laundry room"]
    },
    {
        "name": "Sanford Riley Hall",
        "dormID": 8,
        "address": "108 Institute Rd",
        "rating": 0,
        "tags": ["first-year", "communal bathroom", "singles", "doubles"]
    },
    {
        "name": "Stoddard Complex",
        "dormID": 9,
        "address": "109 Institute Rd",
        "rating": 0,
        "tags": ["first-year", "communal bathroom", "singles", "doubles"]
    },
    {
        "name": "WPI Townhouses",
        "dormID": 10,
        "address": "110 Institute Rd",
        "rating": 0,
        "tags": ["first-year", "communal bathroom", "singles", "doubles"]
    },
    {
        "name": "Wachusett House",
        "dormID": 11,
        "address": "111 Institute Rd",
        "rating": 0,
        "tags": ["first-year", "private bathroom", "house", "singles", "doubles"]
    },
    {
        "name": "Trowbridge House",
        "dormID": 12,
        "address": "112 Institute Rd",
        "rating": 0,
        "tags": ["upperclass", "private bathroom", "singles", "doubles", "kitchen", "laundry room"]
    },
]

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

reviews = [
    {
        "userID": 1,
        "roomSize": 4,
        "diningProximity": 4,
        "academicProximity": 4,
        "amenities": 4,
        "comment": 4,
        "dormID": 4
    }, 
    
    {
        "userID": 2,
        "roomSize": 0,
        "diningProximity": 0,
        "academicProximity": 0,
        "amenities": 0,
        "comment": "bro this sucks",
        "dormID": 4
    }
        
]

users = [
    {
        "username": "smccarty",
        "password": "12345",
        "userID": 1
    },
    {
        "username": "jdoe",
        "password": "abc",
        "userID": 2
    }
]

db["dorms"].insert_many(buildings)
db["reviews"].insert_many(reviews)
db["users"].insert_many(users)

# all_dorms = db["dorms"].count_documents({})  # find() with no filter returns everything

# for dorm in all_dorms:
#     print(dorm)

print("done")