from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.sql import func
from database import Base  

class UserQuery(Base):
    __tablename__ = "user_queries"

    id = Column(Integer, primary_key=True, index=True)
    destination_id = Column(Integer, ForeignKey("cities.id"), nullable=True)
    origin_id = Column(Integer, ForeignKey("cities.id"), nullable=True)
    budget = Column(Integer, nullable=True)
    travel_date = Column(DateTime, nullable=True)
    transport_id = Column(Integer, ForeignKey("transport_means.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    transport_option_id = Column(Integer, ForeignKey("transport_options.id"), nullable=True)
    session_id = Column(String, index=True)
