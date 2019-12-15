#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

""" The first state model """


Base = declarative_base()
""" The Base variable """


class State(Base):
    """ The State Model """
    __table__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String)
