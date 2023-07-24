""" William Eckert 7/23/2023 """

""" drop test user """
DROP USER IF EXISTS 'bill'@'localhost';

"""creates user"""
CREATE USER 'bill'@'localhost' IDENTIFIED WITH mysql_native_password BY "123456";

"""Grants all privileges to database"""
GRANT ALL PRIVILEGES ON pysports.* TO'bill'@'localhost';



"""creates the team table"""
CREATE TABLE team (
    team_id INT NOT NULL AUTO_INCREMENT,
    team_name VARCHAR (250) NOT NULL,
    mascot VARCHAR(250) NOT NULL,
    PRIMARY KEY(team_id)
);

"""Creating the player table and sets the foreign key"""
CREATE TABLE player (
    player_id INT NOT NULL, AUTO_INCREMENT,
    first_name VARCHAR(250) NOT NULL,
    last_name VARCHAR(250) NOT NULL,
    team_id INT NOT NULL,
    PRIMARY KEY (player_id),
    CONSTRAINT fk_team
    FOREIGN KEY (team id)
        REFERENCES team(team_id)
);


  """ insert the teams """
INSERT INTO team(team_name, mascot)
    VALUES('Team Radiants', 'Silly Spren');

INSERT INTO team(team_name, mascot)
    VALUES('Team Todium', 'Singing Singers');

""" Droping the tables """
DROP TABLE IF EXISTS player;

"""Selects the Team id """

SELECT team_id FROM team WHERE team_name = 'Team Todium'


"""Import the Statements"""
IMPORT mysql.connector
from mysql.connector import errorcode

"""Configuring the Database"""
config = {"user": "bill",
    "password": "123456",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Please press any key to continue...")

except mysql.connector.Error as err:
    """ on error code"""

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password is wrong")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()


