from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles # Optional, but good practice
from app.database import engine, Base
from app.routers import user_routes
from app.models import user

# Create Tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Setup Templates
templates = Jinja2Templates(directory="app/templates")

# Include the API Router (The Logic)
app.include_router(user_routes.router)

# ============================
# FRONTEND ROUTES (Moved to Main)
# ============================

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.get("/login-ui", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/profile-ui", response_class=HTMLResponse)
async def profile_page(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})

@app.get("/register-ui", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})