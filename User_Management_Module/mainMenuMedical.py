import Authentication_Authorization_Module.inputValidation as iv
import Notifications_Module.appointmentManager as apt
import Device_Interface_Module.menuDevices as dm

from requests import post, get, delete
import sqlite3
import os

# url that's hosting the User API
url = "http://localhost:8000/user/"

# The directory to the path that the users database will be stored
dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "User_Management_Module", "users.db")

# Stores the available medical professional menu option numbers. Must be updated if any options are added/removed
medical_Options = [1,2,3,4]

# Stores the available device menu option numbers. Must be updated if any options are added/removed
devices_menu = [1,2,3]

# Brings up the medical professional menu, and returns the command the user gave (after input sanitation)
def mainMenuMedical():

    while True:

        print("****** How Can We Help Today? ****** \n")
        print("[1]: My Patients")
        print("[2]: Appointment Management")
        print("[3]: Device Management")
        print("[4]: Log Out \n")
        print("************************************ \n")

        command = input("Enter a Command Based on the Numbers above: ")
        san_command = iv.sanitizeOptions(command)
        if san_command == "Invalid":
            continue
        elif san_command not in medical_Options:
            print("Enter a Valid Command \n")
            continue
        else: 
            match san_command:
                case 1: 
                    print("Patient List Accessed \n")

                    user_table_connect = sqlite3.connect(dir_path)
                    user_cur = user_table_connect.cursor()
                    user_cur.execute("SELECT * from users where role = 4")
                    results = user_cur.fetchall()

                    print("User ID | First Name | Last Name ")
                    for i in results:
                        print(i[0], "       ", i[1], "       ", i[2], " \n")

                    user_cur.close()
                    user_table_connect.close()

                    continue
                case 2: 
                    apt.appointManage()
                    continue
                case 3: 
                    
                    print("************ Device Menus ************ \n")
                    print("[1]: All Devices Menu")
                    print("[2]: User Devices Menu")
                    print("[3]: Go Back \n")
                    print("************************************** \n")

                    device_menu_selection = input("Which menu Would you like to access?: ")
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

                    continue
                case 4:
                    print("Logging Out \n")
                    break