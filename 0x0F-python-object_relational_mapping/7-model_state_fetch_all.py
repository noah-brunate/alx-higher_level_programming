#!/usr/bin/python3
"""
script that lists all State objects from the
database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)

    Session = session()
    result = Session.query(State).order_by(State.id).all()

    for val in result:
        print("{}: {}".format(val.id, val.name))
