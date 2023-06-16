#!/usr/bin/python3
"""script displays values in the states table of hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    displays values where name matches the argument
    """

    conn = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306,
        passwd=argv[2], db=argv[3])

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
        ORDER BY states.id ASC".format(argv[4]))

    results = cursor.fetchall()
    for val in results:
        print(val)
