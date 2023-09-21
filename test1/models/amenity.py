#!/usr/bin/python3
""" This script describes the Amenity Class"""

from os import getenv
import models
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """The base model that Represents Amenity """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128),
                      nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """This code initializes Amenity"""
        super().__init__(*args, **kwargs)
