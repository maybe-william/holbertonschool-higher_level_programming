#!/usr/bin/python3
""" The first city model """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
""" The Base variable """
from model_state import State

class City(Base):
    """ The City Model """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey(State.id))
