import sqlite3
import os

# The directory to the path that the users database will be stored
dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "User_Management_Module", "healthcare.db")

def create_Database():

    # Create database.db table if it doesn't already exist. Source: https://docs.python.org/3/library/sqlite3.html
    db_connect = sqlite3.connect("healthcare.db")
    db_cur = db_connect.cursor()

    db_cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        ssn INT NOT NULL, 
        email TEXT NOT NULL,                         
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role INT NOT NULL)''')

    db_cur.execute('''
    CREATE TABLE IF NOT EXISTS devices (
        id INT PRIMARY KEY,
        device_name TEXT NOT NULL,
        device_type TEXT NOT NULL)''')
    
    db_cur.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INT PRIMARY KEY,
        patient_id INT NOT NULL,
        doctor_id INT NOT NULL,
        appointment_date TEXT NOT NULL,
        appointment_time TEXT NOT NULL,
        time_entered TEXT NOT NULL)''')

    db_connect.commit()

    db_connect.close()