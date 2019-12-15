#!/usr/bin/python3
import MySQLdb
from sys import argv

""" This module lists entries in a table that match a name sans SQLi"""

if __name__ == '__main__':
    # argv: 1 is username, 2 is pass, 3 is db name
    sql = MySQLdb.connect(host="localhost", port=3306,
                          user=argv[1], passwd=argv[2], db=argv[3])
    x = argv[4].split("'")[0]
    cur = sql.cursor()
    s = "SELECT c.name FROM cities c LEFT JOIN states s ON "
    s = s + "c.state_id = s.id WHERE s.name = '{}' ORDER BY c.id ASC".format(x)
    cur.execute(s)
    rows = cur.fetchall()
    if argv[4] == x:
        print(", ".join([x[0] for x in rows]))
    cur.close()
    sql.close()
