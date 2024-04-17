import re
import pytest

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
    

########################################################################################
######################### Unit Tests Defined Below #####################################
########################################################################################


######## Checking sanitizeText Function ########

# Contains a string of alphabet characters (upper and lowercase) only
def test_sanitizeText_alphabet_only():
    assert sanitizeText("HealthCare") == "HealthCare"

# Contains a string with numeric characters only
def test_sanitizeText_numbers_only():
    assert sanitizeText("8675309") == "8675309"

# Contains a string with alphabetic and numeric characters
def test_sanitizeText_mixed():
    assert sanitizeText("rdude10101") == "rdude10101"

# Contains a space, an unallowed character
def test_sanitizeText_with_spaces():
    assert sanitizeText("Very Cool") == "Invalid"

# No input/empty string
def test_sanitizeText_empty():
    assert sanitizeText("") == "Invalid"

# Contains special characters, which are not allowed
def test_sanitizeText_with_special_chars():
    assert sanitizeText("D@RR+#") == "Invalid"


######### Checking santitizeOptions Function ##########

# Contains regular number input between 0-9
def test_sanitizeOptions_valid_number():
    assert sanitizeOptions("3") == 3

# Contains a string of alphabetic characters (not allowed)
def test_sanitizeOptions_text_string():
    assert sanitizeOptions("two") == "Invalid"

# No input/empty string
def test_sanitizeOptions_empty():
    assert sanitizeOptions("") == "Invalid"

# Contains a negative number
def test_sanitizeOptions_negative_number():
    assert sanitizeOptions("-1") == "Invalid"

# Contains special characters
def test_sanitizeOptions_negative_number():
    assert sanitizeOptions("[2]") == "Invalid"

# Contains a number outside of the options 0-9
def test_sanitizeOptions_too_large():
    assert sanitizeOptions("20") == "Invalid"


######## Checking sanitizeNames Function ########

# Contains a string of alphabet characters (upper and lowercase) only
def test_sanitizeNames_alphabet_only():
    assert sanitizeNames("Omar") == "Omar"

# Contains a string with numeric characters only
def test_sanitizeNames_numbers_only():
    assert sanitizeNames("98765") == "Invalid"

# Contains a string with alphabetic and numeric characters
def test_sanitizeNames_mixed():
    assert sanitizeNames("Jeff2024") == "Invalid"

# Contains a space, an unallowed character
def test_sanitizeNames_with_spaces():
    assert sanitizeNames("Professor Darrow") == "Invalid"

# No input/empty string
def test_sanitizeNames_empty():
    assert sanitizeNames("") == "Invalid"

# Contains special characters, which are not allowed
def test_sanitizeNames_with_special_chars():
    assert sanitizeNames("C@$hM[0]ney") == "Invalid"


######### Checking santitizeSSN Function ##########

# Contains a number of valid SSN length and numeric values only
def test_sanitizeSSN_valid_SSN():
    assert sanitizeSSN("900800700") == 900800700

# Contains a string of alphabetic characters (not allowed)
def test_sanitizeSSN_text_string():
    assert sanitizeSSN("eigthy") == "Invalid"

# Contains a string with alphabetic and numeric characters (not allowed)
def test_sanitizeSSN_mixed():
    assert sanitizeSSN("myssnis1234") == "Invalid"

# No input/empty string
def test_sanitizeSSN_empty():
    assert sanitizeSSN("") == "Invalid"

# Contains a negative number of valid SSN length
def test_sanitizeSSN_negative_number():
    assert sanitizeSSN("-100200300") == "Invalid"

# Contains special characters
def test_sanitizeSSN_special_characters():
    assert sanitizeSSN("***-**-****") == "Invalid"

# Contains a number shorter than valid SSN
def test_sanitizeSSN_short():
    assert sanitizeSSN("654738") == "Invalid"

# Contains a number longer than valid SSN
def test_sanitizeSSN_short():
    assert sanitizeSSN("10000000000000000") == "Invalid"


######### Checking santitizeEmail Function ##########

# Contains a valid email address
def test_sanitizeEmail_valid_email():
    assert sanitizeEmail("darrowry@bu.edu") == "darrowry@bu.edu"

# Missing an @ symbol for the email
def test_sanitizeEmail_no_at_symbol():
    assert sanitizeEmail("darrow.ryan.s.gmail.com") == "Invalid"

# Missing a proper domain
def test_sanitizeEmail_missing_domain():
    assert sanitizeEmail("tom_brady_12@") == "Invalid"

# Contains unallowed special characters
def test_sanitizeEmail_invalid_characters():
    assert sanitizeEmail("thebest!email@yahoo.com") == "Invalid"

# No input/empty string
def test_sanitizeEmail_empty():
    assert sanitizeEmail("") == "Invalid"