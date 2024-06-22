#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL username, password and database name from arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=db_name)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute a SQL query to select all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
