#!/usr/bin/python3
"""script that lists all states with a name starting with N hbtn_0e_0_usa"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    queries the database for states starting with N
    """

    conn = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306,
        passwd=argv[2], db=argv[3])

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
        ORDER BY states.id ASC")

    results = cursor.fetchall()

    for val in results:
        print(val)
