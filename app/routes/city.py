from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.city import City
from app.schemas.city import CityCreate, CityUpdate, CityOut
from app.database import get_db

router = APIRouter(prefix="/cities", tags=["cities"])

# Create a new city
@router.post("/", response_model=CityOut)
def create_city(city: CityCreate, db: Session = Depends(get_db)):
    existing_city = db.query(City).filter(func.lower(City.name) == city.name.lower()).first()
    if existing_city:
        raise HTTPException(status_code=400, detail="City already exists")
    new_city = City(**city.model_dump())
    db.add(new_city)
    db.commit()
    db.refresh(new_city)
    return new_city

# Get all cities
@router.get("/", response_model=list[CityOut])
def get_all_cities(db: Session = Depends(get_db)):
    cities = db.query(City).all()
    return cities

# Get city by name
@router.get("/{city_name}", response_model=CityOut)
def get_city_by_name(city_name: str, db: Session = Depends(get_db)):
    city = db.query(City).filter(func.lower(City.name) == city_name.lower()).first()
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city