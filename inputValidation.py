import re

# Sanitizes text inputs so that improper commands cannot be entered for future table queries
# Only allows users to give non-special character inputs
def sanitizeText(text):
    if not re.match("^[a-zA-Z0-9]*$", text):
        print("Enter valid text")
        return "Invalid"
    else:
        return text

# Sanitizes option menu inputs so that only numerical options be given
# Only allows users to enter values between 0-9
def sanitizeOptions(num):
    if not re.match("^[0-9]*$", num):
        print("Enter a Number")
        return "Invalid"
    else:
        return int(num)
    
# Used to sanitize name inputs. Only allows for lowercase and uppercase letters
# Note: this may need to be adjusted, as there are names with -
def sanitizeNames(text):
    if not re.match("^[a-zA-Z]*$", text):
        return "Invalid"
    else:
        return text
    
# Used to sanitize the Social Security input. Assumes no - in the input. 
# Returns "Invalid" if letters are entered or the length of the SSN doesn't match normal length (9)
def sanitizeSSN(num):
    if not re.match("^[0-9]*$", num):
        print("Enter numbers only")
        return "Invalid"  
    elif len(num) != 9:
        print("Incorrect Length for SSN. Try Again")
        return "Invalid"
    else:
        return int(num)

# Used to sanitize the email input. Allows for some special characters generally seen in emails (@_. to start) 
# Note: may need to be adjusted to support additional characters
def sanitizeEmail(email):
    if not re.match("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", email):
        print("Enter valid text")
        return "Invalid"
    else:
        return email