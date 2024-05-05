import Authentication_Authorization_Module.inputValidation as iv
from datetime import datetime

import sqlite3
import os

# The directory to the path that the users database will be stored
# The double os.path.dirname used to jump to parent directory (Health-Monitoring-System-API)
dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "User_Management_Module", "healthcare.db")

# Stores the available patient menu option numbers. Must be updated if any options are added/removed
appointment_Options = [1,2,3]

# Stores the available patient menu option numbers. Must be updated if any options are added/removed
scheduling_Options = [1,2,3,4]

# Creates an appointment for a patient
def createAppt():

    # Establish database connection 
    appt_table_connect = sqlite3.connect(dir_path)
    appt_curr = appt_table_connect.cursor()

    try:
        # Check for existing devices and get max ID
        appt_curr.execute("SELECT MAX(id) from appointments")
        result = appt_curr.fetchone()
        if result[0] is not None:
            id = result[0] + 1
        else:
            id = 1

        while True:
            patient = input("Enter Patient ID: ")

            if patient.strip() == "":  # Check for empty input
                print("Patient ID cannot be empty. Try again")
                continue
            else:
                break

        while True:
            doctor = input("Enter Doctor ID: ")
            
            if doctor.strip() == "":  # Check for empty input
                print("Doctor ID cannot be empty. Try again")
                continue
            else:
                break

        while True:
            date = input("Enter Date of Appointment: ")
            
            if date.strip() == "":  # Check for empty input
                print("Date cannot be empty. Try again")
                continue
            else:
                break

        while True:
            time = input("Enter Time of Appointment: ")
            
            if time.strip() == "":  # Check for empty input
                print("Date cannot be empty. Try again")
                continue
            else:
                break

        try:

            entered_time = datetime.now()
            formatted_time = entered_time.strftime('%Y-%m-%d %H:%M:%S')

            command = """INSERT INTO appointments (id, patient_id, doctor_id, appointment_date, appointment_time, time_entered) VALUES (?, ?, ?, ?, ?, ?)"""
            appt_curr.execute(command, (id, patient, doctor, date, time, formatted_time))

            appt_table_connect.commit()  
            print("Appointment Added Successfully! \n")
        except:
            print("Appointment ID not found. Try again \n")
        

    except sqlite3.Error as err:
        print(f"Error Scheduling Appointment: {err}") 
    finally:
        # Close connection regardless of exceptions
        appt_curr.close()
        appt_table_connect.close()

    return

def cancelAppt():
    appt_table_connect = sqlite3.connect(dir_path)
    appt_curr = appt_table_connect.cursor()

    try:
        while True:
            
            delete_id = input("Enter the ID of the appointment to cancel: ")
                
            if delete_id.strip() == "":  # Check for empty input
                print("Appointment ID cannot be empty. Try again")
                continue
            else:
                break

        # Delete device with the specified ID
        command = "DELETE FROM appointments WHERE id = ?"
        appt_curr.execute(command, (int(delete_id),))

        appt_table_connect.commit()
        print(f"Appoitnment cancelled successfully.\n")

    except sqlite3.Error as err:
        print(f"Error: {err}")  # Print specific error message
    finally:
        # Close connection regardless of exceptions
        appt_curr.close()
        appt_table_connect.close()

# Lists the appointments based on a given Doctor ID (meant to be used by Doctor/Nurse)
def listAppts():

    appt_table_connect = sqlite3.connect(dir_path)
    appt_cur = appt_table_connect.cursor()

    doctor = input("Enter your Doctor ID: ")

    sql_command = """SELECT * from appointments where doctor_id = ?"""

    appt_cur.execute(sql_command, (doctor,))
    results = appt_cur.fetchall()

    print("Patient ID | Date | Time")
    for i in results:
        print(i[1], "       ", i[3], "       ", i[4], " \n")

    appt_cur.close()
    appt_table_connect.close()

    return

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

        if command.strip() == "":  # Check for empty input
            print("Command cannot be empty. Try again")
            continue

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
                    createAppt()
                    continue
                case 2: 
                    print("Please select the Appointment you would like to change: \n")
                    continue
                case 3: 
                    cancelAppt()
                    continue
                case 4:
                    print("Returning... \n")
                    break


# The appointment menu for Doctors to view upcoming appointments or schedule appointments
def appointManage():

    while True:

        print("****** Appointment Manager ****** \n")
        print("[1]: View Upcoming Appointments")
        print("[2]: Schedule/Reschedule an Appointment")
        print("[3]: Return to Main Menu \n")
        print("************************************ \n")

        command = input("Enter a Command Based on the Numbers above: ")

        if command.strip() == "":  # Check for empty input
            print("Command cannot be empty. Try again")
            continue

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
                    listAppts()
                    continue
                case 2: 
                    schedulingAppt()
                    continue
                case 3:
                    print("Returning to Main Menu...")
                    break

