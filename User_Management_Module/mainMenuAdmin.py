import Authentication_Authorization_Module.inputValidation as iv
import Device_Interface_Module.menuDevices as dm

import sqlite3
import os

# url that's hosting the User API
url = "http://localhost:8000/user/"

# The directory to the path that the users database will be stored
dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "User_Management_Module", "healthcare.db")

# Stores the available medical professional menu option numbers. Must be updated if any options are added/removed
admin_Options = [1,2,3,4]

# Stores the available device menu option numbers. Must be updated if any options are added/removed
devices_menu = [1,2,3]

# Brings up the medical professional menu, and returns the command the user gave (after input sanitation)
def mainMenuAdmin():

    while True:

        print("************ Hello Admin ************ \n")
        print("[1]: User Management")
        print("[2]: Device Management")
        print("[3]: Log Out \n")
        print("************************************* \n")

        command = input("Enter a Command Based on the Numbers above: ")

        if command.strip() == "":  # Check for empty input
            print("Command cannot be empty. Try again")
            continue

        san_command = iv.sanitizeOptions(command)

        if san_command == "Invalid":
            continue
        
        elif san_command not in admin_Options:
            print("Enter a Valid Command \n")
            continue
        else: 
            match san_command:
                case 1: 
                    print("User List Accessed \n")

                    user_table_connect = sqlite3.connect(dir_path)
                    user_cur = user_table_connect.cursor()
                    user_cur.execute("SELECT * from users")
                    results = user_cur.fetchall()

                    print("User ID | First Name | Last Name | Email      | Username")
                    for i in results:
                        print(i[0], "       ", i[1], "       ", i[2], "       ", i[4], "       ", i[5], " \n")

                    continue
                case 2: 

                    print("************ Device Menus ************ \n")
                    print("[1]: Device Menu")
                    print("[2]: Users Devices Menu")
                    print("[3]: Go Back \n")
                    print("************************************** \n")

                    device_menu_selection = input("Which menu Would you like to access?: ")

                    if device_menu_selection.strip() == "":  # Check for empty input
                        print("Command cannot be empty. Try again")
                        continue

                    san_command = iv.sanitizeOptions(device_menu_selection)
                    if san_command == "Invalid":
                        continue
                    elif san_command not in devices_menu:
                        print("Enter a Valid Command \n")
                        continue
                    else:
                        match san_command:
                            case 1:
                                dm.mainMenuDevices_Data()
                            case 2:
                                dm.mainMenuDevices_User()
                            case 3:
                                continue

                case 3:
                    print("Logging Out \n")
                    break