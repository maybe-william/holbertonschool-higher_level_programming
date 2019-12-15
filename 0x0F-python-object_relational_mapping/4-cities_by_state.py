#!/usr/bin/python3
import MySQLdb
from sys import argv

""" This module lists entries in a table that match a name sans SQLi"""

if __name__ == '__main__':
    # argv: 1 is username, 2 is pass, 3 is db name
    sql = MySQLdb.connect(host="localhost", port=3306,
                          user=argv[1], passwd=argv[2], db=argv[3])

    cur = sql.cursor()
    s = "SELECT c.id, c.name, s.name FROM cities c LEFT JOIN states s"
    s = s + " ON c.state_id = s.id ORDER BY c.id ASC"
    cur.execute(s)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    sql.close()
