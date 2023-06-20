#!/usr/bin/python3
"""
contains the class definition of a State and
an instance Base = declarative_base()
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class States(Base):
    """
    This class:
     -inherites from Base
     -links to the MySQL table states
     -with class attribute id that represents a column
     -class attribute name that represents a column of a string
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
