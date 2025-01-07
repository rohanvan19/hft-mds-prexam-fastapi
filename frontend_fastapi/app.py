from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import httpx
import os

# Initialize FastAPI app
app = FastAPI()
templates = Jinja2Templates(directory="/workspaces/hft-mds-prexam-fastapi/frontend_fastapi/templates")

# Base URL for the Spring Boot API
SPRING_BOOT_API_URL = os.getenv("SPRING_BOOT_API_URL", "http://localhost:8080/api/shoppingItems")

# Home Page: Display all shopping items
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(SPRING_BOOT_API_URL)
        if response.status_code == 200:
            items = response.json()  # Get the list of items from the API
            #flash_message = None
        else:
            items = []  # If the API fails, show an empty list

    except Exception as e:
        items = []  # If there's an exception, show an empty list

    # Render the template with the fetched items and flash message
    return templates.TemplateResponse("index.html", {
        "request": request,
        "items": items,
    })

# Add a new shopping item
@app.get("/add", response_class=HTMLResponse)
async def add_item_form(request: Request):
    return templates.TemplateResponse("add_item.html", {"request": request})

@app.post("/add")
async def add_item(name: str = Form(...), amount: int = Form(...)):
    payload = {"name": name, "amount": amount}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(SPRING_BOOT_API_URL, json=payload)
        if response.status_code in [200, 201]:
            return RedirectResponse(url="/", status_code=303)
        else:
            raise HTTPException(status_code=500, detail="Failed to add item.")
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to connect to the backend.")

# Update an existing shopping item
@app.get("/update/{name}", response_class=HTMLResponse)
async def update_item_form(request: Request, name: str):
    return templates.TemplateResponse("update_item.html", {"request": request, "name": name})

@app.post("/update/{name}")
async def update_item(name: str, amount: int = Form(...)):
    payload = {"name": name, "amount": amount}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(f"{SPRING_BOOT_API_URL}/{name}", json=payload)
        if response.status_code == 200:
            return RedirectResponse(url="/", status_code=303)
        else:
            raise HTTPException(status_code=500, detail="Failed to update item.")
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to connect to the backend.")

# Delete a shopping item
@app.get("/delete/{name}")
async def delete_item(name: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"{SPRING_BOOT_API_URL}/{name}")
        if response.status_code == 204:
            return RedirectResponse(url="/", status_code=303)
        else:
            raise HTTPException(status_code=500, detail="Failed to delete item.")
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to connect to the backend.")