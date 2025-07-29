from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import relationship
from database import Base

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    region = Column(String, nullable=True)
    country = Column(String)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float,  nullable=True)
    description = Column(Text, nullable=True)

    # Relationships
    origin_queries = relationship("UserQuery", back_populates="origin_city", foreign_keys="UserQuery.origin_id")
    destination_queries = relationship("UserQuery", back_populates="destination_city", foreign_keys="UserQuery.destination_id")
    
    hotels = relationship("Hotel", back_populates="city", cascade="all, delete-orphan")

    origin_routes = relationship("TransportRoute", back_populates="origin_city", foreign_keys="TransportRoute.origin_city_id")
    destination_routes = relationship("TransportRoute", back_populates="destination_city", foreign_keys="TransportRoute.destination_city_id")
