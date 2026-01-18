from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import json

from mongo_db import db, reviews, trigger_overall_ratings

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/create-review", response_class=HTMLResponse)
async def add_review(request: Request):
    query = db["dorms"].find({})
    dorm_names = [dorm["name"] for dorm in query]
    return templates.TemplateResponse("review.html", {"request": request, "dorm_names": dorm_names})

@app.get("/search-dorms", response_class=HTMLResponse)
async def to_dorm(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})

class SearchRequest(BaseModel):
    search: str

@app.post("/search-dorms")
async def dorms(req: SearchRequest):
    # Get the search string from the request
    search_text = req.search.strip()

    if search_text != "all":
        # Query with partial match (case-insensitive)
        query = list(db["dorms"].find({"name": {"$regex": search_text, "$options": "i"}}))

        if not query:  # search by tag, partial match
            query = db["dorms"].find({
                "tags": {"$elemMatch": {"$regex": search_text, "$options": "i"}}
            })
    else:
        query = db["dorms"].find({})

    results = [dorm["name"] for dorm in query]

    return {"results": results}

# Dynamic dorm page route
@app.get("/dorm-review/{dorm_name}", response_class=HTMLResponse)
async def dorm_review(request: Request, dorm_name: str):
    # Here, you would fetch dorm info from your database
    # dorm_info = get_dorm_info(dorm_name)  # <-- replace with your actual DB call
    # query = {"name": dorm_name}

    # query_filter = {"name": dorm_name}
    # projection = {"_id": 1}
    # document = collection.find_one(query_filter, projection)

    dorm = db["dorms"].find_one({"name": dorm_name.strip()})
    dormID = dorm.get("dormID")
    overall_rating = db["overall_ratings"].find_one({"dormID": dormID})
    reviews = db["reviews"].find({"dormID": dormID})

    return templates.TemplateResponse(
        "dorms.html",
        {
            "request": request,
            "dorm_name": dorm_name,
            "tags": dorm["tags"],
            "overall_rating": overall_rating,
            "reviews": reviews
        }
    )

# Example helper (replace with real DB)
def get_dorm_info(name):
    ...
    return ...

@app.get("/housing-info", response_class=HTMLResponse)
async def housing_info(request: Request):
    return templates.TemplateResponse("housing.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/get-review", response_class=HTMLResponse)
async def add_review(request: Request):
    return templates.TemplateResponse("review.html", {"request": request})

@app.post("/submit-review")
async def submit_review(
    dorm: str = Form(...),
    room_rating: int = Form(...),
    acad_rating: int = Form(...),
    dine_rating: int = Form(...),
    amen_rating: int = Form(...),
    comment: str = Form(...)
):
    # add to database
    dormID = db["dorms"].find_one({"name": dorm.strip()}).get("dormID")
    rating = {
        "roomSize": room_rating,
        "diningProximity": dine_rating,
        "academicProximity": acad_rating,
        "amenities": amen_rating,
        "comment": comment,
        "dormID": dormID
    }
    reviews.insert_one(rating)
    trigger_overall_ratings(dormID)
    # print(rating)
    # Redirect to home page after submission
    return RedirectResponse(url="/", status_code=303)