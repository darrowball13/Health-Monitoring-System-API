import Authentication_Authorization_Module.inputValidation as iv

# Stores the available patient menu option numbers. Must be updated if any options are added/removed
patient_Options = [1,2,3,4]

# Brings up the patient menu, and returns the command the user gave (after input sanitation)
def mainMenuPatient():

    print("Main Menu: \n")
    print("[1]: My Medical Infomation")
    print("[2]: Billing Information")
    print("[3]: Appointment Management")
    print("[4]: Log Out \n")

    while True:
        command = input("Enter a Command Based on the Numbers above: ")
        san_command = iv.sanitizeOptions(command)
        if san_command == "Invalid":
            continue
        elif san_command not in patient_Options:
            print("Enter a Valid Command")
            continue
        else: 
            break

    match san_command:
        case 1: 
            print("Medical Information Accessed")
        case 2: 
            print("Billing Information Accessed")
        case 3: 
            print("Appiontment Manager Accessed")
        case 4:
            print("Logging Out")