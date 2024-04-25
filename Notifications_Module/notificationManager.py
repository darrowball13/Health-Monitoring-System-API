import threading
import queue
import sqlite3
import os

# url that's hosting the User API
url = "http://localhost:8000/user/"

# The directory to the path that the users database will be stored
# The double os.path.dirname used to jump to parent directory (Health-Monitoring-System-API)
dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "User_Management_Module", "users.db")

# Reference: https://docs.python.org/3/library/queue.html

q = queue.Queue()

def notify_Users_access():
    while True:
        item = q.get()
        user_role = item[-1]

        match user_role:
            case 1:
                print("Role: Admin - Can Read/Write Data, Add/Remove Patients and Devices, Edit Database Structure, Edit Code")
            case 2:
                print(f"Role: Doctor - Can Read/Write Data, Add/Remove Patients and Devices")
            case 3:
                print(f"Role: Nurse - Can Read/Write Data, Add/Remove Patients and Devices (Limited Basis)")
            case 4:
                print(f"Role: Patient - Can Read/Write Data for Yourself Only")

        q.task_done()

# Begin threads for each notificaiton
threading.Thread(target=notify_Users_access, daemon=True).start()

user_table_connect = sqlite3.connect(dir_path)
user_cur = user_table_connect.cursor()
user_cur.execute("SELECT * from users")
results = user_cur.fetchall()

user_cur.close()
user_table_connect.close()

# Send all notification requests out
for item in results:
    q.put(item)

# Block until all tasks are done
q.join()
print('All notifications sent')
