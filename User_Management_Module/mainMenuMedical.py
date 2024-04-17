import Authentication_Authorization_Module.inputValidation as iv
import Notifications_Module.appointmentManager as apt

# Stores the available medical professional menu option numbers. Must be updated if any options are added/removed
medical_Options = [1,2,3,4]

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
                    continue
                case 2: 
                    apt.appointManage()
                    continue
                case 3: 
                    print("Appiontment Manager Accessed \n")
                    continue
                case 4:
                    print("Logging Out \n")
                    break