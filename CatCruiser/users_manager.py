import sqlite3

def create_users_table(): #creates the table users.db if it does not already exist
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Users
        (Username VARCHAR PRIMARY KEY,
        Password VARCHAR NOT NULL)""")

def new_user(Username, Password): #creates a new user in Users
    database = sqlite3.connect("database.db")
    c = database.cursor()
    try:
        c.execute("""INSERT INTO Users VALUES (?, ?)""", (Username, Password))
    except:
        return False
    database.commit() #commits the changes to the database
    database.close() #closes the database

def check_if_password_is_correct(Username, Password): #checks to see if password is correct
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""SELECT * FROM Users WHERE Username = ? AND Password = ? """, (Username, Password))
    #selects username and password if both are matching
    login = c.fetchall()
    if login == []: #if no combination of username and password exists in table, login variable is empty
        return False #returns False
    else:
        return True

def update_username(Username, newUsername, Password):
    if check_if_password_is_correct(Username, Password) == False:
        return "Incorrect password!"
    else:
        database = sqlite3.connect("database.db")
        c = database.cursor()
        c.execute("""UPDATE Users SET Username = ? WHERE Username = ? AND Password = ?""", (newUsername, Username, Password))
        database.commit()
        database.close()
        return "Password changed successfully!"

