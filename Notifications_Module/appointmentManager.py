import Authentication_Authorization_Module.inputValidation as iv

# Stores the available patient menu option numbers. Must be updated if any options are added/removed
appointment_Options = [1,2,3]

# Stores the available patient menu option numbers. Must be updated if any options are added/removed
scheduling_Options = [1,2,3,4]

# Handles making, canceling, and rescheduling appointments
def schedulingAppt():

    while True:
        print("****** What would you like to do? ****** \n")
        print("[1]: Schedule an Appointment")
        print("[2]: Change an Appointment")
        print("[3]: Cancel an Appointment")
        print("[4]: Return to Appointment Manager \n")
        print("**************************************** \n")

        command = input("Enter a Command Based on the Numbers above: ")
        san_command = iv.sanitizeOptions(command)
        if san_command == "Invalid":
            continue
        elif san_command not in scheduling_Options:
            print("Enter a Valid Command \n")
            continue
        else: 
            match san_command:
                case 1: 
                    print("Please enter Appointment information below: \n")
                    continue
                case 2: 
                    print("Please select the Appointment you would like to change: \n")
                    continue
                case 3: 
                    print("Please select the Appointment you would like to cancel: \n")
                    continue
                case 4:
                    print("Returning... \n")
                    break


# Brings up the patient menu, and returns the command the user gave (after input sanitation)
def appointManage():

    while True:

        print("****** Appointment Manager ****** \n")
        print("[1]: View Upcoming Appointments")
        print("[2]: Schedule/Reschedule an Appointment")
        print("[3]: Return to Main Menu \n")
        print("************************************ \n")

        command = input("Enter a Command Based on the Numbers above: ")
        san_command = iv.sanitizeOptions(command)
        if san_command == "Invalid":
            continue
        elif san_command not in appointment_Options:
            print("Enter a Valid Command")
            continue
        else: 
            match san_command:
                case 1: 
                    print("Upcoming Appointments Below: \n")
                    continue
                case 2: 
                    schedulingAppt()
                    continue
                case 3:
                    print("Returning to Main Menu...")
                    break