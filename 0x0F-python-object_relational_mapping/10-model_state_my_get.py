#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import text


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    Session = session()

    result = Session.query(State).filter(text("States.name=:val"),
        params(val=sys.argv[4])).order_by(State.id).all()

    for num in result:
        if num is None:
            print("Not found")
        else:
            print(num.id)
