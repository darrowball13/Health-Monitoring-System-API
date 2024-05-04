from Authentication_Authorization_Module import inputValidation as iv
from Authentication_Authorization_Module import checkCredentials as check
from requests import get
import sqlite3
import os

# url that's hosting the User API
url = "http://localhost:8000/user/"

# The directory to the path that the users database will be stored
dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "User_Management_Module", "healthcare.db")

# print(dir_path)

def login():

    print("Please enter the following information: ")

    # Username
    while True:
        username = input("Username: ")

        if username.strip() == "":  # Check for empty input
            print("Command cannot be empty. Try again")
            continue

        username = iv.sanitizeText(username)
        if username == "Invalid":
            print("Enter a valid username")
            continue
        elif not check.checkUsernameExists(username):
            print("Username not found")
            continue
        else: 
            break
    
    # Password
    while True:
        password = input("Password: ")

        if password.strip() == "":  # Check for empty input
            print("Command cannot be empty. Try again")
            continue

        password = iv.sanitizeText(password)
        if password == "Invalid":
            print("Enter a valid password")
            continue
        else: 
            break

    # Query SQL database to determine User ID number (primary key) based on username
    user_table_connect = sqlite3.connect(dir_path)
    user_cur = user_table_connect.cursor()
    user_cur.execute(f"SELECT * FROM users WHERE username =?", (username,))
    test = user_cur.fetchall()

    uid = test[0][0]
    user_table_connect.close()

    result = get(url+str(uid)).json()
    if result["password"] == password:
        return True, username, result["role"]
    else:
        return False, username, result["role"]

