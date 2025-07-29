from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base  

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True)
    sender = Column(String) # e.g., "user" or "system"
    content = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_query_id = Column(Integer, ForeignKey("user_queries.id"), nullable=True)
    extracted_fields = Column(String, nullable=True)

    # Relationship
    user_query = relationship("UserQuery", back_populates="messages")
