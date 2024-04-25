"""
Author: Elicia Ramitt

Usage: python createAccounts.py

Description: Initializes the database for all accounts, creates new accounts, adds to the database
"""

# Import statements
import os
import sqlite3

# Main Function for testing
def main():
    filePath = getFilePath()
    print(createDatabase(filePath))
    addAccount(filePath, "Joey Ma", "qwerty", 100)
    # Return Statement
    return 0

# Function for finding the file path for the database
def getFilePath():
    """Gets the absolute file path of the database

    Returns:
        string: file path of the database
    """
    # Get the script's directory
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    # Get the database path
    databasePath = os.path.join(scriptDir, "accounts.db")
    
    # Return the full path of the file path
    return databasePath

# Function for creating the database
def createDatabase(databasePath):
    """Initializes the database if it is not already created
    
    Args:
        databasePath (str): path of the database
    """
    # Check if the database already exists
    if not os.path.isfile(databasePath):
        # Create connection
        con = sqlite3.connect(databasePath)
        # Create cursor
        cur = con.cursor()
        
        # Create the query
        accountQuery = """
        CREATE TABLE IF NOT EXISTS accounts
        (
            id  INTEGER PRIMARY KEY,
            name    TEXT NOT NULL,
            password    TEXT NOT NULL,
            balance INTEGER
        );
        """
        
        # Execute and close
        cur.execute(accountQuery)
        con.commit()
        con.close()
        # Tell user it was a success
        print("Database successfully created.")
        
    # Else...tell user it already exists
    else:
        print("Database already exists.")
        
# Function to add account to the database
def addAccount(databasePath, name, password, balance):
    """Adds account to the database

    Args:
        databasePath (string): the absolute path for the database
        name (string): the name of the user
        password (string): user's password
        balance (int): user's balance
    """
    # Create a connection to the database
    con = sqlite3.connect(databasePath)
    # Create cursor
    cur = con.cursor()
    # Execute with the information provided by the user
    cur.execute("INSERT INTO accounts (name, password, balance) VALUES (?, ?, ?)", (name, password, balance))
    # Close the connection and commit
    con.commit()
    con.close()
    
    # Tell user the account was added.
    print("Account successfully added.")
    
# Python Incantation
if __name__ == "__main__":
    main()