from fastapi import FastAPI
from app.routes import city

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Travel API running"}

app.include_router(city.router)
