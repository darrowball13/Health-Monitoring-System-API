import Authentication_Authorization_Module.inputValidation as iv

# Stores the available patient menu option numbers. Must be updated if any options are added/removed
patient_Options = [1,2,3,4]

# Brings up the patient menu, and returns the command the user gave (after input sanitation)
def mainMenuPatient():

    while True:

        print("****** How Can We Help Today? ****** \n")
        print("[1]: My Medical Infomation")
        print("[2]: Billing Information")
        print("[3]: Appointment Management")
        print("[4]: Log Out \n")
        print("************************************ \n")

        command = input("Enter a Command Based on the Numbers above: ")

        if command.strip() == "":  # Check for empty input
            print("Command cannot be empty. Try again")
            continue

        san_command = iv.sanitizeOptions(command)
        if san_command == "Invalid":
            continue
        elif san_command not in patient_Options:
            print("Enter a Valid Command \n")
            continue
        else: 
            match san_command:
                case 1: 
                    print("Medical Information Accessed \n")
                    continue
                case 2: 
                    print("Billing Information Accessed \n")
                    continue
                case 3: 
                    print("Appiontment Manager Accessed \n")
                    continue
                case 4:
                    print("Logging Out \n")
                    break