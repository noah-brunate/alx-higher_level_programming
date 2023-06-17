#!/usr/bin/python3
"""script prevents sql injection through user input"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    detects sql injection
    """
    sql = "SELECT * FROM states WHERE name LIKE BINARY %(name)s\
        ORDER BY states.id ASC"

    conn == MySQLdb.connect(
        host="localhost", user=argv[1], port=3306,
        passwd=argv[2], db=argv[3])

    cursor = conn.cursor()

    cursor.execute(sql, {'name': argv[4]})

    results = cursor.fetchall()
    for val in results:
        print(val)
