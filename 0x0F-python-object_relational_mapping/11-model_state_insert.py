#!/usr/bin/python3
"""
Script that adds the State object to database
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb//{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    Session = session()
    obj = State(name='Louisiana')
    Session.add(obj)
    Session.commit()
    result = Session.query(State).filter(State.name == 'Louisiana').first()

    for num in result:
        print(num.id)
