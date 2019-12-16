#!/usr/bin/python3
""" The first state model """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
""" The Base variable """


class State(Base):
    """ The State Model """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cities = relationship("City", backref="state")
