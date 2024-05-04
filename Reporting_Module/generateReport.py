import threading
import queue
import sqlite3
import os

# url that's hosting the User API
url = "http://localhost:8000/user/"

# The directory to the path that the users database will be stored
# The double os.path.dirname used to jump to parent directory (Health-Monitoring-System-API)
dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "User_Management_Module", "healthcare.db")

# Reference: https://docs.python.org/3/library/queue.html

q = queue.Queue()

def Report_Generation():
    while True:
        item = q.get()
        print(f'Info: {item}')
        q.task_done()

threading.Thread(target=Report_Generation, daemon=True).start()

user_table_connect = sqlite3.connect(dir_path)
user_cur = user_table_connect.cursor()
user_cur.execute("SELECT * from users")
results = user_cur.fetchall()

user_cur.close()
user_table_connect.close()

for item in results:
    q.put(item)

# Block until all tasks are done.
q.join()
print('All reports completed')
