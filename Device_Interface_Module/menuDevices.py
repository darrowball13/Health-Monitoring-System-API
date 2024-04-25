import Authentication_Authorization_Module.inputValidation as iv

# Stores the available device-user relationship menu option numbers. Must be updated if any options are added/removed
device_menu_users = [1,2,3,4]

# Stores the available device-database option numbers. Must be updated if any options are added/removed
device_menu_data = [1,2,3,4]

# Brings up the menu for device management for database, and returns the command the user gave (after input sanitation)
def mainMenuDevices_Data():

    while True:

        print("****** Device Management Menu ****** \n")
        print("[1]: Find a Device")
        print("[2]: Register a Device")
        print("[3]: Remove a Device")
        print("[4]: Back to Main Menu \n")
        print("************************************ \n") 

        command = input("Enter a Command Based on the Numbers above: ")
        san_command = iv.sanitizeOptions(command)
        if san_command == "Invalid":
            continue
        elif san_command not in device_menu_data:
            print("Enter a Valid Command \n")
            continue
        else: 
            match san_command:
                case 1: 
                    print("Enter Device ID/Name: \n")
                    continue
                case 2: 
                    print("Please enter the device information below: \n")
                    
                    continue
                case 3: 
                    print("Enter Device ID/Name: \n")
                    continue
                case 4:
                    print("Returning to Main Menu... \n")
                    break

# Brings up the menu for user-device relationship management. and returns the command the user gave (after input sanitation)
def mainMenuDevices_User():

    while True:

        print("****** Users-Devices Management Menu ****** \n")
        print("[1]: Check User Devices")
        print("[2]: Add a Device to a User")
        print("[3]: Remove a Device from a User")
        print("[4]: Back to Main Menu \n")
        print("****************************************** \n")

        command = input("Enter a Command Based on the Numbers above: ")
        san_command = iv.sanitizeOptions(command)
        if san_command == "Invalid":
            continue
        elif san_command not in device_menu_users:
            print("Enter a Valid Command \n")
            continue
        else: 
            match san_command:
                case 1: 
                    print("Enter User ID/Name: \n")
                    continue
                case 2: 
                    print("Enter the User to which you want to add a device: \n")
                    continue
                case 3: 
                    print("Enter the User to which you want to remove a device: \n")
                    continue
                case 4:
                    print("Returning to Main Menu... \n")
                    break