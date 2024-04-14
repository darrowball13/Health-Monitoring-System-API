from requests import get
import sqlite3
import os

# url that's hosting the User API
url = "http://localhost:8000/user/"

# The directory to the path that the users database will be stored
# The double os.path.dirname used to jump to parent directory (Health-Monitoring-System-API)
dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "User_Management_Module", "users.db")

print(dir_path)

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
    
def checkEmailExists(email):

    # Query SQL database to determine User ID number (primary key) based on username
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
    
def checkSSNExists(ssn):

    # Query SQL database to determine User ID number (primary key) based on username
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
    
# print(checkUsernameExists("kdarrow1"))