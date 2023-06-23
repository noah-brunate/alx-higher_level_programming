#!/usr/bin/python3

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

session = sessionmaker(bind=engine)
Session = session()

result = Session.query(States).first()

if result == None:
    print("Nothing")
else:
    print("{}: {}".format(result.id, result.name))
