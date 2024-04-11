import signInMenu as sim
import registrationForm as reg
import mainMenuPatient as mmp
import Authentication_Authorization_Module as auth

# Sanitizes text inputs so that improper commands cannot be entered for future table queries
# Only allows users to give non-special character inputs
# def sanitizeText(text):
#     if not re.match("^[a-zA-Z0-9]*$", text):
#         print("Enter valid text")
#         return "Invalid"
#     else:
#         return text

# # Sanitizes option menu inputs so that only numerical options be given
# # Only allows users to enter values between 0-9
# def sanitizeOptions(num):
#     if not re.match("^[0-9]*$", num):
#         print("Enter a Number")
#         return "Invalid"
#     else:
#         return int(num)

def main():

    print("Welcome to Darrow Health! \n")

    # Keeps app open unless "Exit" command is entered
    while True:

        # Brings up the sign in menu and returns the option chose by the user, which is used by the case statement
        # to determine the next action(s)
        signIn = sim.signIn()

    
        # Note: need to confirm the options here map to the proper options in the sign in menu
        match signIn:
            case 1:
                print("Log In Accessed")

                # Put Log In Authentication Here
                # if authorized: 
                print("Welcome [Name]!")
                mmp.mainMenuPatient()
                # else
                # print("Invalid Log In Credentials. Try Again")
                continue 
            case 2:
                print("Please Fill Out the Following Infomation: \n")
                firstname, lastname, ssn, username, password, email, role = reg.register()
                print ("Registered with the following info: \n")
                print ("Name: " + firstname +  " " + lastname)
                print ("SSN: " + str(ssn))
                print ("Username: " + username)
                print ("Password: " + password)
                print ("Email: " + email)

                match role:
                    case 1:
                        print("Role: Admin \n")
                    case 2:
                        print("Role: Doctor \n")
                    case 3:
                        print("Role: Nurse/Non-Doctor Medical Professional \n")
                    case 4:
                        print("Role: Patient \n")

                print("Returning to Main Menu... \n")

                continue
            case 3: 
                print("Goodbye!")
                break 
    
if __name__ == '__main__':
    main()