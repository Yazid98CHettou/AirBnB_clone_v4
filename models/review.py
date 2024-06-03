#!/usr/bin/python3
"""class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """__tablename__ (str): table to store Reviews.
        text: The review description.
        place_id: review's place id.
        user_id: review's user id.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

