""" 
    Title: pysports_update_and_delete.py
    Author: William Eckert
    Date: 7/23/2023
    Description: Test program for editing records from the pysports database
"""

""" importing statements """
import mysql.connector
from mysql.connector import errorcode


""" database config """
config = {
    "user": "bill",
    "password": "123456",
    "host": "10.0.0.23",
    "database": "pysports",
    "raise_on_warnings": True
}


def show_players(cursor, title):
    """ exeecuting unner join and iterating over the dataset and output the results to the terminal window.
       
    """

    # inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get the results from the cursor object 
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    # iterate over the player data set and display the results 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    """ try/catch block for handling potential errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 

    # getting the cursor object
    cursor = db.cursor()

    # inserting player query 
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    # player data fields 
    player_data = ("Hoid", "Team Themselves?", 1)

    # inserting a new player record
    cursor.execute(add_player, player_data)

    # committing the insert to the database 
    db.commit()

    # showing all records in the player table 
    show_players(cursor, "DISPLAYING ALL PLAYERS AFTER INSERT")

    # updating the newly inserted record 
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Wit', last_name = 'Wandererman' WHERE first_name = 'Hoid'")

    # executing the update query
    cursor.execute(update_player)

    # showing all records in the player table 
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # deleting the query 
    delete_player = ("DELETE FROM player WHERE first_name = 'Wit'")

    cursor.execute(delete_player)

    # showing all records in the player table 
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETION")

    input("\n\n Please press any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The database does not exist")

    else:
        print(err)

finally:
    """ closing the connection to MySQL """

    db.close()