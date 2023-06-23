#!/usr/bin/python3
"""
Script that Changes the name of the State where id = 2 to New Mexico
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if _name__ == '__main__':
    eng = create_engine("myql+mysql://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(eng)
    session = sessionmaker(bind=eng)
    Session = session()

    obj = Session.query(State).filter(State.id == 2).first()
    obj.name = 'New Mexico'
    Session.commit()
    Sesson.close()
