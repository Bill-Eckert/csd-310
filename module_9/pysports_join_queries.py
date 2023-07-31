""" 
    Title: pysports_join_queries.py
    Author: William Eckert
    Date: July 30, 2023
    Description: Test program for joining the two tables
"""

""" importing statements """
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "bill",
    "password": "123456",
    "host": "10.0.0.23",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    
    """ try/catch any errors in database """ 

    db = mysql.connector.connect(**config) 
    # connecting to the pysports database 

    cursor = db.cursor()

    # the inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # getting the results from the cursor object 
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")
    
    # printing the player and team names
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    """ handling any errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  This database does not exist")

    else:
        print(err)

finally:
    """ closing the connection """

    db.close()