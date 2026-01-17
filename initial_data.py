from mongo_db import db

db["dorms"].delete_many({})

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

db["dorms"].insert_many(buildings)

all_dorms = db["dorms"].count_documents({})  # find() with no filter returns everything

# for dorm in all_dorms:
#     print(dorm)

print(all_dorms)