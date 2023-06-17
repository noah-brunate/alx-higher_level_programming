#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    should take 3 arguments: mysql username, mysql password and database name
    """

    conn = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                           passwd=argv[2], db=argv[3])

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cities")

    results = cursor.fetchall()
    for val in results:
        print(val)
