from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from mongo_db import db, reviews, trigger_overall_ratings

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def add_review(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/create-review", response_class=HTMLResponse)
async def add_review(request: Request):
    return templates.TemplateResponse("review.html", {"request": request})

@app.get("/search-dorms", response_class=HTMLResponse)
async def to_dorm(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})

class SearchRequest(BaseModel):
    search: str

@app.post("/search-dorms")
async def dorms(req: SearchRequest):
    # Get the search string from the request
    search_text = req.search.strip()

    # Query with partial match (case-insensitive)
    query = db["dorms"].find({"name": {"$regex": search_text, "$options": "i"}})
    results = [dorm.get("name") for dorm in query]
    print(results)

    return {"results": results}

# Dynamic dorm page route
@app.get("/search")
async def search(request: Request, query: str = ""):
    search_term = query.strip()
    
    # Query MongoDB for the exact name (case-insensitive)
    dorm = db.dorms.find_one({
        "name": {"$regex": f"^{search_term}$", "$options": "i"}
    })
    
    if dorm:
        # Redirect to the specific dorm page (e.g., /dorms/morgan)
        return RedirectResponse(url=f"/dorms/{dorm['id']}")
    
    # If not found, send them back to the dorms list
    return RedirectResponse(url="/dorms")

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