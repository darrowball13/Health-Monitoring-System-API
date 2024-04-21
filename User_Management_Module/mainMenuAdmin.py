import Authentication_Authorization_Module.inputValidation as iv
import Device_Interface_Module.menuDevices as dm

# Stores the available medical professional menu option numbers. Must be updated if any options are added/removed
admin_Options = [1,2,3,4]
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
        san_command = iv.sanitizeOptions(command)
        if san_command == "Invalid":
            continue
        elif san_command not in admin_Options:
            print("Enter a Valid Command \n")
            continue
        else: 
            match san_command:
                case 1: 
                    print("Patient List Accessed \n")
                    continue
                case 2: 

                    print("************ Device Menus ************ \n")
                    print("[1]: Device Data Menu")
                    print("[2]: Users-Devices Menu")
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

                case 3:
                    print("Logging Out \n")
                    break