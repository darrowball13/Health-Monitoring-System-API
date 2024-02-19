from User_Management_Module import checkUserType

'''
Checks the UserType to determine what kind of report to generate. For this, I'm assuming patients and their caregivers don't need
as much detailed medical info as the doctors and nurses. May add section for customized reports if given the time
'''

def reportType(User):

    userType = checkUserType(User)

    ReportType = 0
    
    return ReportType

'''
Calls the appropriate report type to generate, based on ReportType given from reportType function above
'''

def gerateReport(ReportType):

    # Temporary placeholder for choosing report

    if ReportType == 0:
        basicReport()

    else: medicalReport()

    return
 

def basicReport():

    return

def medicalReport():

    return