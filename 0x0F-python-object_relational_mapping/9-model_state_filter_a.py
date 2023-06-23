#!/usr/bin/python3

from sys import argv
from sqlalchemy import create_egine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    Session = session()

    result = Session.query(States).filter(States.name.like('%a')).order_by(states.id).all()

    for val in result:
        print("{}: {}".format(result.id, result.name))
    Session.close()
