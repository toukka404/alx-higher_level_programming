#!/usr/bin/python3
""" takes name of a state as an argument and lists all cities of that state,
    SQL injection free!
"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id=states.id WHERE states.name=%s""",
                (sys.argv[4], ))
    query_rows = cur.fetchall()
    answers = []
    for row in query_rows:
        answers.append(row[0])
    print(', '.join(answers))
    cur.close()
    conn.close()
