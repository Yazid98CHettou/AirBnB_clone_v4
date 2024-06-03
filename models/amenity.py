#!/usr/bin/python3
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
class Amenity(BaseModel, Base):
    """Amenity Represents"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'database' else ''
