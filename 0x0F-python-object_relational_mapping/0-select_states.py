#!/usr/bin/python3

"""
Script that lists all states from the database hbtn_0e_0_usa.
Parameters for script: mysql username, mysql password, database name.
Must use the 'MySLdb' Module.
Script should connect to a MySQL server running on 'localhost' at port '3306'Results must be in ascending order by 'states.id'.
Code should not be executed when imported.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    #secure connection esterblished to connect the MySQL
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    #creating a cursor object to excute sqla 

    cursor db.cursor()
    cursor.execute("SELECT *FROM states ORDER BY ID ASC")
    #fetchig all the result
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()S
