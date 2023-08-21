#!/usr/bin/python3
"""MODULE DOCSTRING"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                        user=sys.argv[1],
                        password=sys.argv[2],
                        dbName=sys.argv[3],
                        port="3306")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
