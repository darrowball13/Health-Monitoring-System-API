from User_Management_Module import checkUserType

def accessPatientList(User):

    UserType = checkUserType(User)

    # temporary definition

    if UserType == 0:
        return True
 
    return False