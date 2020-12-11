#!/usr/bin/python3
""" Lists all states from a database """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    nmrows = cur.execute("SELECT id,name FROM `states`")
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
            
