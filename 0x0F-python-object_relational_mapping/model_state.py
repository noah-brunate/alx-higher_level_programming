#!/usr/bin/python3
"""
contains the class definition of a State and
an instance Base = declarative_base()
"""

from sqlalchemy import create_engine, column, integer, string
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

    id = column(integer, primary_key=True, nullable=False)
    name = column(string(128), nullable=False)
