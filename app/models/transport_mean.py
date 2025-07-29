from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class TransportMean(Base):
    __tablename__ = "transport_means"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # Relationships
    transport_options = relationship("TransportOption", back_populates="means", cascade="all, delete-orphan")
    user_queries = relationship("UserQuery", back_populates="transport")

    def __repr__(self):
        return f"<TransportMean(name={self.name})>"
