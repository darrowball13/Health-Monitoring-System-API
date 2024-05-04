import signInMenu as sim
import User_Management_Module.registrationForm as reg
import User_Management_Module.mainMenuPatient as mmp
import User_Management_Module.mainMenuMedical as mmm
import User_Management_Module.mainMenuAdmin as mma
import Authentication_Authorization_Module.logInForm as li
from requests import post, get, delete
import sqlite3
import os

# url that's hosting the User API
url = "http://localhost:8000/user/"

# The directory to the path that the users database will be stored
dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "User_Management_Module", "healthcare.db")

def main():

    print("Welcome to Darrow Health! \n")

    # Keeps app open unless "Exit" command is entered
    while True:

        # Brings up the sign in menu and returns the option chose by the user, which is used by the case statement
        # to determine the next action(s)
        signIn = sim.signIn()

        # Note: need to confirm the options here map to the proper options in the sign in menu
        match signIn:
            case 1:
                print("Log In Accessed")

                logInCheck, user, user_role = li.login()
                if logInCheck:
                    print(f"Welcome {user}!")

                    if user_role == 1:
                        mma.mainMenuAdmin()
                    elif user_role == 2 or user_role == 3:
                        mmm.mainMenuMedical()
                    elif user_role == 4:
                        mmp.mainMenuPatient()
                    else:
                        print("Invalide User Role. Please reach out to an Admin to fix.")
                        continue
                        
                else:
                    print(f"Invalid Log In Credentials for {user} . Try Again")
                    continue 
            case 2:
                print("Please Fill Out the Following Infomation: \n")

                # Uses register() function to return sanitized inputs for 
                firstname, lastname, ssn, username, password, email, role = reg.register()

                # Checks to make sure the table isn't empty. If it is, sets uid to 1
                user_table_connect = sqlite3.connect(dir_path)
                user_cur = user_table_connect.cursor()
                user_cur.execute("SELECT MAX(id) from users")
                result_2 = user_cur.fetchone()
                try:
                    uid = result_2[0]+1
                
                except:
                    uid = 1

                user_cur.close()
                user_table_connect.close()

                # Tries to add User to users.db
                try:
                    print(post(url+str(uid), json={"first_name" : firstname, "last_name" : lastname, "ssn" : ssn, 
                                               "email" : email, "username" : username, "password" : password, "role" : role}))
                except Exception as e:
                    print(f"ERROR: Failed to create user:", e)

                print ("Registered with the following info: \n")
                print ("Name: " + firstname +  " " + lastname)
                print ("SSN: " + str(ssn))
                print ("Username: " + username)
                print ("Password: " + password)
                print ("Email: " + email)

                match role:
                    case 1:
                        print("Role: Admin \n")
                    case 2:
                        print("Role: Doctor \n")
                    case 3:
                        print("Role: Nurse/Non-Doctor Medical Professional \n")
                    case 4:
                        print("Role: Patient \n")

                print("Returning to Main Menu... \n")

                continue
            case 3: 
                print("Goodbye!")
                break 
    
if __name__ == '__main__':
    main()