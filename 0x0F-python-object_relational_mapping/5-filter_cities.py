#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all its cities"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    lists all cities of that state, using the database hbtn_0e_4_usa
    """

    conn = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                           passwd=argv[2], db=argv[3])

    cursor = conn.cursor()

    cursor.execute("SELECT cities.name FROM cities ", {'name': argv[4]})
