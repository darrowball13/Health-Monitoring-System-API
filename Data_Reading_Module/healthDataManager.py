
from datetime import datetime

import sqlite3
import os

# The directory to the path that the users database will be stored
# The double os.path.dirname used to jump to parent directory (Health-Monitoring-System-API)
dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "User_Management_Module", "healthcare.db")


def addHealthData():
    # Establish database connection 
    health_table_connect = sqlite3.connect(dir_path)
    health_curr = health_table_connect.cursor()

    try:
        # Check for existing health records and get max ID
        health_curr.execute("SELECT MAX(id) from healthData")
        result = health_curr.fetchone()
        if result[0] is not None:
            id = result[0] + 1
        else:
            id = 1

        while True:
            patientID = input("Enter your Patient ID: ")

            if patientID.strip() == "":  # Check for empty input
                print("Patient ID cannot be empty. Try again")
                continue
            else:
                break

        while True:
            deviceID = input("Enter the Device ID: ")
            
            if deviceID.strip() == "":  # Check for empty input
                print("Device ID cannot be empty. Try again")
                continue
            else:
                break

        while True:
            healthInfo = input("Enter the value of the measurement: ")
            
            if healthInfo.strip() == "":  # Check for empty input
                print("Value cannot be empty. Try again")
                continue
            else:
                break

        try:

            entered_time = datetime.now()
            formatted_time = entered_time.strftime('%Y-%m-%d %H:%M:%S')

            command = """INSERT INTO healthData (id, patient_id, device_id, value, time_entered) VALUES (?, ?, ?, ?, ?)"""
            health_curr.execute(command, (id, patientID, deviceID, healthInfo, formatted_time))

            health_table_connect.commit()  
            print("Data Added Successfully! \n")
        except:
            print("Error adding Data. Try again \n")
        

    except sqlite3.Error as err:
        print(f"Error Adding Data: {err}") 
    finally:
        # Close connection regardless of exceptions
        health_curr.close()
        health_table_connect.close()

    return


def listHealthData():

    health_table_connect = sqlite3.connect(dir_path)
    health_curr = health_table_connect.cursor()

    pid = input("Enter your Patient ID: ")

    sql_command = """SELECT * from healthData where patient_id = ?"""

    health_curr.execute(sql_command, (pid,))
    results = health_curr.fetchall()

    print("Device ID | Value | Time Recorded")
    for i in results:
        print(i[2], "       ", i[3], "       ", i[4], " \n")

    health_curr.close()
    health_table_connect.close()

    return



