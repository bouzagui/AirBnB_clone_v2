#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

class City(BaseModel, Base):
    """ The city class, contains state ID and name
    Attributes:
        name: The name of the city
        state_id: The state ID of the city
    """
    __tablename__ = 'cities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='city', cascade='all, delete-orphan')
