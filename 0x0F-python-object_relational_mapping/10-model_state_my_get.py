#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import text


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}\
                           :{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bimd=engine)
    Session = session()

    result = Session.query(States).filter(text("States.name=:val"), params(val=sys.argv[4]))

    if result == None:
        print("Not found")
    else:
        print(result.id)
    Session.close()
