"""
    Author: Elicia Ramitt
    
    Usage: python bankViewer.py
    
    Description: Adding a tkinter viewer to my program
"""

# Import statements
from tkinter import Tk, ttk
import createAccounts
import accountManagement
import ctypes

# Create the database
databasePath = createAccounts.getFilePath()
createAccounts.createDatabase(databasePath)

# create a root
root = Tk()
root.title("Bank Management")

# Set Icon
iconID = 'BankAcount.bankViewer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(iconID)
root.iconbitmap('bankICON.ico')

# FRAMES
credentialFrame = ttk.Frame(root)
credentialFrame.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

createAccountFrame = ttk.Frame(root)
createAccountFrame.grid(row=0, column=3, columnspan=3, padx=10, pady=10)

balanceFrame = ttk.Frame(root)
balanceFrame.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# WIDGETS
enterName = ttk.Label(credentialFrame, text="Name:")
enterName.grid(padx=10, pady=10)
enterPass = ttk.Label(credentialFrame, text="Password:")
enterPass.grid(padx=10, pady=10, row=1, column=0)
nameEntry = ttk.Entry(credentialFrame)
nameEntry.grid(padx=10, pady=10, row=0, column=1)
passEntry = ttk.Entry(credentialFrame)
passEntry.grid(padx=10, pady=10, row=1, column=1)

# log in button click
def loginClick():
    # Get the name
    name = nameEntry.get()
    # Get the password
    password = passEntry.get()
    # Login
    status = accountManagement.logIn(name, password)
    # Check if it was successful
    if status:
        balLabel = ttk.Label(balanceFrame, text=status)
        balLabel.grid(row=0, column=0, padx=10, pady=10)
    else:
        failureLabel = ttk.Label(balanceFrame, text="Login Failed. Please either re-enter your username and password or create an account.")

loginBtn = ttk.Button(credentialFrame, text="Login", command=loginClick)
loginBtn.grid(padx=25, pady=10, row=1, column=2)

enterName = ttk.Label(createAccountFrame, text="Name:")
enterName.grid(padx=10, pady=10)
enterPass = ttk.Label(createAccountFrame, text="Password:")
enterPass.grid(padx=10, pady=10, row=1, column=0)
nameEntry = ttk.Entry(createAccountFrame)
nameEntry.grid(padx=10, pady=10, row=0, column=1)
passEntry = ttk.Entry(createAccountFrame)
passEntry.grid(padx=10, pady=10, row=1, column=1)
enterBal = ttk.Label(createAccountFrame, text="Balance:")
enterBal.grid(padx=10, pady=10)
balEntry = ttk.Entry(createAccountFrame)
balEntry.grid(padx=10, pady=10, row=2, column=1)

loginBtn = ttk.Button(createAccountFrame, text="Create Account")
loginBtn.grid(padx=25, pady=10, row=2, column=2)
root.mainloop()