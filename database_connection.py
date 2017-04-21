#!/usr/bin/python
import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="test_db_user",         # your username
                     passwd="test_db_pwd",  # your password
                     db="test_db")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM employee")

numrows = cur.rowcount

print "Number of rows " + str(numrows)

filename = "out.txt"

print "Opening the file..."
target = open(filename, 'w')


# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0],row[1]
    target.write("%s\t%s\t%s\n" % (row[0],row[1],row[2]));

target.close()

db.close()
