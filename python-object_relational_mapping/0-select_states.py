#!/usr/bin/python3
"""MODULE DOCSTRING"""

import sys
import MySQLdb

def command(argument):
    db = MySQLdb.connect(host = "localhost",
                        user = argument[0],
                        password = argument[1], 
                        dbName = argument[2],
                        port = "3306")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
