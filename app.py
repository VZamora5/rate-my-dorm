from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from mongo_db import json_to_review

from mongo_db import db, reviews, trigger_overall_ratings

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/create-review", response_class=HTMLResponse)
async def add_review(request: Request):
    return templates.TemplateResponse("review.html", {"request": request})

@app.get("/dorms", response_class=HTMLResponse)
async def to_dorm(request: Request):
    return templates.TemplateResponse("dorms.html", {"request": request})

@app.get("/housing-info", response_class=HTMLResponse)
async def housing_info(request: Request):
    return templates.TemplateResponse("housing.html", {"request": request})

@app.get("/get-review", response_class=HTMLResponse)
async def add_review(request: Request):
    return templates.TemplateResponse("review.html", {"request": request})

@app.post("/submit-review")
async def submit_review(
    dorm: str = Form(...),
    rating: int = Form(...),
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