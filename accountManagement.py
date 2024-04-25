"""
    Author: Elicia Ramitt
    
    Usage: python accountManagement.py
    
    Description: Different account management: logging in, delete account,
"""

# Import Statements
import sqlite3
import createAccounts

# Main Function for Testing
def main():
    return 0

# Log In Function
def logIn(name, password):
    """Allows for the user to log into their account. Confirms that their credentials are valid

    Args:
        name (str): the name for the account
        password (str): the password for the account
        
    Returns:
        balance (int): the balance attached to the account
    """
    # Get the database path
    databasePath = createAccounts.getFilePath()
    # Create the connection
    con = sqlite3.connect(databasePath)
    # Cursor
    cur = con.cursor()
    # Get the password of the account holder
    cur.execute("SELECT password FROM acconuts WHERE name = ?", (name,))
    # Fetch the password
    pswd = cur.fetchone()
    # See if it is the same
    if pswd == password:
        # Print success statement
        print("Login successful.")
        # Get the balance
        cur.execute("SELECT balance FROM accounts WHERE password = ?", (password,))
        # Fetch thr balance
        balance = cur.fetchone()
        # Return the balance
        return balance
    # If the passwords are not the same, do not log in
    else:
        # Print failure.
        print("Login unsuccessful.")
        # Return None
        return None
    
    # Close the connection
    con.close()
    
# Python Incantation
if __name__ == "__main__":
    main()