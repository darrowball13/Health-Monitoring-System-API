import inputValidation as iv
import re

# Stores the available role option numbers. Must be updated if any roles are added/removed
Roles = [1,2,3,4]


# Begins getting the user inputs in order to add their information to the Users database
# For every variable, the input is sanitized before moving onto the next one, allowing the user to retry immediately
# Note that if the structure of the Users database is changed, this will need to be adjusted accordingly
def register():

    # First name 
    while True:
        first_name = input("First Name: ")
        first_name = iv.sanitizeNames(first_name)
        if first_name == "Invalid":
            print("Enter a valid first name")
            continue
        else: 
            break
    
    # Last name
    while True:
        last_name = input("Last Name: ")
        last_name = iv.sanitizeNames(last_name)
        if last_name == "Invalid":
            print("Enter a valid last name")
            continue
        else: 
            break

    # Social Security Number
    while True:
        ssn = input("Social Security Number (enter with no -): ")
        ssn = iv.sanitizeSSN(ssn)
        if ssn == "Invalid":
            print("Enter a valid SSN")
            continue
        else: 
            break
    
    # Username
    while True:
        username = input("Username: ")
        username = iv.sanitizeText(username)
        if username == "Invalid":
            print("Enter a valid username")
            continue
        else: 
            break
    
    # Password
    while True:
        password = input("Password: ")
        password = iv.sanitizeText(password)
        if password == "Invalid":
            print("Enter a valid username")
            continue
        else: 
            break

    # Email
    while True:
        email = input("Email: ")
        email = iv.sanitizeEmail(email)
        if email == "Invalid":
            print("Enter a valid email")
            continue
        else: 
            break

    print("\n")

    # Begins the process of adding the primary role for the user

    print("[1]: Admin")
    print("[2]: Docter")
    print("[3]: Nurse/Non-Doctor Medical Professinal")
    print("[4]: Patient \n")

    while True:
        primary_role = input("What is your primary role? (More may be added after registration): ")
        san_role = iv.sanitizeOptions(primary_role)
        if san_role == "Invalid":
            continue
        elif san_role not in Roles:
            print("Enter a Valid Role Number")
            continue
        else: 
            break

    return first_name, last_name, ssn, username, password, email, san_role
