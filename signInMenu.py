import inputValidation as iv

# Stores the available sign in option numbers. Must be updated if any options are added/removed
sign_In_Options = [1,2,3]

# Brings up the sign in menu for the user, and returns the command the user gave (after input sanitation)
def signIn():

    print("*********** Main Menu *********** \n")
    print("[1]: Log In")
    print("[2]: Register")
    print("[3]: Exit \n")
    print("********************************* \n")
 
    while True:
        command = input("Enter a Command Based on the Numbers above: ")
        san_command = iv.sanitizeOptions(command)
        if san_command == "Invalid":
            continue
        elif san_command not in sign_In_Options:
            print("Enter a Valid Command")
            continue
        else: 
            break

    return san_command