#!/usr/bin/python3
"""User class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ __tablename__ (str): The name of the MySQL table to store users.
        email: user's email address.
        password:user's password.
        first_name :user's first name.
        last_name:user's last name.
        places:User-Place relationship.
        reviews: User-Review relationship.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")

