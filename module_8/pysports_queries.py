
    Title: pysports_queries.py
    Author: William Eckert
    Date: 15 July 2023
    Description: pysports database testing
"""

""" import my statements """
import mysql.connector
from mysql.connector import errorcode

""" database configuration """
config = {
    "user": "bill",
    "password": "123456",
    "host": "10.0.0.23",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 

    cursor = db.cursor()

    # select query from the team table 
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # get the results from the cursor object 
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING THE TEAMS --")
    
    # iterate over the teams data set and display the results 
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    # select query for the player table 
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # get the results from the cursor object 
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING THE PLAYERS --")

    # iterate over the players data set and display the results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n Please press any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are incorrect")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """
    
    db.close()