from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from mongo_db import db

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/add-review", response_class=HTMLResponse)
async def add_review(request: Request):
    return templates.TemplateResponse("review.html", {"request": request})

@app.get("/dorms", response_class=HTMLResponse)
async def to_dorm(request: Request):
    return templates.TemplateResponse("dorms.html", {"request": request})

@app.get("/housing-info", response_class=HTMLResponse)
async def housing_info(request: Request):
    return templates.TemplateResponse("housing.html", {"request": request})