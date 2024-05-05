import Authentication_Authorization_Module.inputValidation as iv
import Data_Reading_Module.healthDataManager as health

# Stores the available device-user relationship menu option numbers. Must be updated if any options are added/removed
data_menu_health = [1,2,3]

# Brings up the menu for health data management. and returns the command the user gave (after input sanitation)
def mainMenuHealthData():

    while True:

        print("****** Medical Information Menu ****** \n")
        print("[1]: Check My Health Data")
        print("[2]: Add New Measurement")
        print("[3]: Back to Main Menu \n")
        print("****************************************** \n")

        command = input("Enter a Command Based on the Numbers above: ")

        if command.strip() == "":  # Check for empty input
            print("Command cannot be empty. Try again")
            continue

        san_command = iv.sanitizeOptions(command)
        if san_command == "Invalid":
            continue
        elif san_command not in data_menu_health:
            print("Enter a Valid Command \n")
            continue
        else: 
            match san_command:
                case 1: 
                    health.listHealthData()
                    continue
                case 2: 
                    print("Please enter the information below: \n")
                    health.addHealthData()
                    continue
                case 3:
                    print("Returning to Main Menu... \n")
                    break