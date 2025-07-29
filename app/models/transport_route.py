from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class TransportRoute(Base):
    __tablename__ = "transport_routes"

    id = Column(Integer, primary_key=True, index=True)
    transport_option_id = Column(Integer, ForeignKey("transport_options.id"), nullable=False)
    origin_city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    destination_city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    price_estimate = Column(String, nullable=True)
    duration = Column(String, nullable=True)
    schedule_info = Column(String, nullable=True)

    # Relationships
    transport_option = relationship("TransportOption", back_populates="routes")
    origin_city = relationship("City", foreign_keys=[origin_city_id], back_populates="origin_routes")
    destination_city = relationship("City", foreign_keys=[destination_city_id], back_populates="destination_routes")

    def __repr__(self):
        return f"<TransportRoute(origin={self.origin_city.name}, destination={self.destination_city.name}, transport_option={self.transport_option.name})>"