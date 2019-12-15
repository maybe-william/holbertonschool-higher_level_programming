#!/usr/bin/python3
import MySQLdb
from sys import argv

# This module lists entries in a table starting with N

if __name__ == '__main__':
    # argv: 1 is username, 2 is pass, 3 is db name
    sql = MySQLdb.connect(host="localhost", port=3306,
                          user=argv[1], passwd=argv[2], db=argv[3])

    cur = sql.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    if len(rows) > 0:
        for row in rows:
            print(row)
    cur.close()
    sql.close()
