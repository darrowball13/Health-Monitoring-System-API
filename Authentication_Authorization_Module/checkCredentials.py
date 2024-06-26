from requests import get
import sqlite3
import os

# url that's hosting the User API
url = "http://localhost:8000/user/"

# The directory to the path that the users database will be stored
# The double os.path.dirname used to jump to parent directory (Health-Monitoring-System-API)
dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "User_Management_Module", "healthcare.db")

# Checks to confirm that the username isn't currently taken, based on users in the users.db database
def checkUsernameExists(username):

    # Query SQL database to determine User ID number (primary key) based on username
    user_table_connect = sqlite3.connect(dir_path)
    user_cur = user_table_connect.cursor()
    user_cur.execute(f"SELECT * FROM users WHERE username =?", (username,))
    exists = user_cur.fetchall()

    user_cur.close()
    user_table_connect.close()

    if exists:
        return True
    else:
        return False
    
# Checks to see if an email has already been taken by a user
def checkEmailExists(email):

    # Query SQL database to determine if email exists in database
    user_table_connect = sqlite3.connect(dir_path)
    user_cur = user_table_connect.cursor()
    user_cur.execute(f"SELECT * FROM users WHERE email =?", (email,))
    exists = user_cur.fetchall()

    user_cur.close()
    user_table_connect.close()

    if exists:
        return True
    else:
        return False

# Checks to see if a SSN has been placed in the users.db table already 
def checkSSNExists(ssn):

    # Query SQL database to determine if SSN exists
    user_table_connect = sqlite3.connect(dir_path)
    user_cur = user_table_connect.cursor()
    user_cur.execute(f"SELECT * FROM users WHERE ssn =?", (ssn,))
    exists = user_cur.fetchall()

    user_cur.close()
    user_table_connect.close()

    if exists:
        return True
    else:
        return False
    
# Checks to see the role of a User 
def getRole(username):

    # Query SQL database to determine User ID number (primary key) based on username
    user_table_connect = sqlite3.connect(dir_path)
    user_cur = user_table_connect.cursor()
    user_cur.execute(f"SELECT * FROM users WHERE username =?", (username,))
    exists = user_cur.fetchall()
    uid = exists[0][0]

    user_cur.close()
    user_table_connect.close()

    if exists:
        result = get(url+str(uid)).json()
        return result["role"]
    else:
        print("User not found. Please try again.")
        return 0