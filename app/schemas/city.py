from pydantic import BaseModel
from typing import Optional

class CityBase(BaseModel):
    name: str
    country:str 
    region: Optional[str] = None
    latitude: float 
    longitude: float
    description: Optional[str] = None

class CityCreate(CityBase):
    pass

class CityUpdate(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    description: Optional[str] = None

class CityOut(BaseModel):
    id: int
    name:str
    country: str
    
    model_config = {
        "from_attributes": True
    }