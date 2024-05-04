import sqlite3
import os
# import Authentication_Authorization_Module.inputValidation as iv

# The directory to the path that the users database will be stored
# The double os.path.dirname used to jump to parent directory (Health-Monitoring-System-API)
dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "User_Management_Module", "healthcare.db")


def addDevice():
    # Establish database connection 
    device_table_connect = sqlite3.connect(dir_path)
    device_cur = device_table_connect.cursor()

    try:
        # Check for existing devices and get max ID
        device_cur.execute("SELECT MAX(id) from devices")
        result = device_cur.fetchone()
        if result[0] is not None:
            id = result[0] + 1
        else:
            id = 1

        while True:
            deviceName = input("Device Name: ")

            if deviceName.strip() == "":  # Check for empty input
                print("Device Name cannot be empty. Try again")
                continue
            else:
                break

        while True:
            deviceType = input("Device Type: ")
            
            if deviceType.strip() == "":  # Check for empty input
                print("Device Type cannot be empty. Try again")
                continue
            else:
                break

        try:
            command = """INSERT INTO devices (id, device_name, device_type) VALUES (?, ?, ?)"""
            device_cur.execute(command, (id, deviceName, deviceType))

            device_table_connect.commit()  
            print("Device Added Successfully! \n")
        except:
            print("Device ID not found. Try again \n")
        

    except sqlite3.Error as err:
        print(f"Error Adding Device: {err}") 
    finally:
        # Close connection regardless of exceptions
        device_cur.close()
        device_table_connect.close()

    return


def deleteDevice():
    device_table_connect = sqlite3.connect(dir_path)
    device_cur = device_table_connect.cursor()

    try:
        while True:
            
            delete_id = input("Enter the ID of the device to delete: ")
                
            if delete_id.strip() == "":  # Check for empty input
                print("Device ID cannot be empty. Try again")
                continue
            else:
                break

        # Delete device with the specified ID
        command = "DELETE FROM devices WHERE id = ?"
        device_cur.execute(command, (int(delete_id),))

        device_table_connect.commit()
        print(f"Device with ID {delete_id} deleted successfully.\n")

    except sqlite3.Error as err:
        print(f"Error: {err}")  # Print specific error message
    finally:
        # Close connection regardless of exceptions
        device_cur.close()
        device_table_connect.close()


def listDevices():

    device_table_connect = sqlite3.connect(dir_path)
    device_cur = device_table_connect.cursor()
    device_cur.execute("SELECT * from devices")
    results = device_cur.fetchall()

    print("Device ID | Device Name | Device Type")
    for i in results:
        print(i[0], "       ", i[1], "       ", i[2], " \n")

    device_cur.close()
    device_table_connect.close()

    return

