from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class TransportOption(Base):
    __tablename__ = "transport_options"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    means_id = Column(Integer, ForeignKey("transport_means.id"), nullable=False)
    website_url = Column(String, nullable=True)

    # Relationships
    means = relationship("TransportMean", back_populates="transport_options")
    routes = relationship("TransportRoute", back_populates="transport_option", cascade="all, delete-orphan")
    user_queries = relationship("UserQuery", back_populates="transport_option")
