from flask import Flask, jsonify, request
from flask_restful import Resource, Api, fields, marshal_with, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os

# THIS MODULE MAY BE DELETED AFTER DISCUSSION IN CLASS TODAY (4/16), AS IT IS UNNECESSARY TO HAVE SEPARATE DATABASES AND
# RESTFUL API'S FOR EVERY SQL TABLE NEEDED. WILL REMAIN FOR NOW WHILE WORKING ON ADJUSTING THE userManagement.py API TO HANDLE
# MULTIPLE TABLES WITHIN A SINGLE DATABASE. THIS ALSO MEANS THE devices.db TABLE WILL MOST LIKELY BE REMOVED AS WELL

# Define flask app and flask_restful API objects
app = Flask(__name__)
api = Api(app)

# Create database.db table if it doesn't already exist. Source: https://docs.python.org/3/library/sqlite3.html
device_table_connect = sqlite3.connect("devices.db")

device_cur = device_table_connect.cursor()

device_cur.execute('''
CREATE TABLE IF NOT EXISTS devices (
    id INT PRIMARY KEY,
    device_name TEXT NOT NULL,
    device_type TEXT NOT NULL)''')

device_table_connect.commit()

device_table_connect.close()

# Configures the userManagement API to connect to the database 'database.db' SQLite file (since SQLite db is locally stored)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'devices.db')
db = SQLAlchemy(app)


# Defines the SQLite table schema with the same name as a db.Model object
class devices(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    device_name = db.Column(db.String(32), nullable = False)
    device_type = db.Column(db.String(32), nullable = False)
    
    def __init__(self, id, device_name, device_type):
        self.id = id
        self.device_name = device_name
        self.device_type = device_type
        

    # Shows what values are returned when this object is queried
    def __repr__(self):
        return self.device_name


# Defines the output data schema
device_definition = {
    'device_id' : fields.Integer,
    'device_name' : fields.String,
    'device_type' : fields.String
}

class FormatUser(object):
    def __init__(self, did, device_name, device_type):
        self.device_id = did
        self.device_name = device_name
        self.device_type = device_type
        
# Define request parser
parser = reqparse.RequestParser()
parser.add_argument('device_name', required=True, help="Device name cannot be blank")
parser.add_argument('device_type', required=True, help="Device type cannot be blank")


def get_device(device_id):
    # If find user, return
    device = devices.query.filter_by(id=device_id).first()

    try:
        if (device):
            return FormatUser(device.id, device.device_name, device.device_type)
        # Otherwise, send error message and error code
        else:
            return {'error' : 'no such device found'}, 404
    except Exception as e:
        print(e) 

# Define a Resource-type class object to define functions for the RESTful API
class UserAPI(Resource):

    # GET function
    @marshal_with(device_definition)
    def get(self, device_id):
        check = devices.query.filter_by(id=device_id).first()
        if not check:
            abort(404, message="Device ID doesn't exist")
        return get_device(device_id)
    
    # PUT / POST function
    @marshal_with(device_definition)
    def post(self, device_id):

        # Parse request for desired values name and secret

        args = parser.parse_args()
        check = devices.query.filter_by(id=device_id).first()
        if check:
            abort(409, message="Device ID taken")
            
        else:
        # Start SQLite db session to insert and commit
            new_user = devices(device_id, args['device_name'], args['device_type'])
            db.session.add(new_user)
            db.session.commit()

        return FormatUser(device_id, args['device_name'], args['device_type'])


    # DELETE function for deleting resources from the API
    def delete(self, device_id):

        # NEW: Use db session to find and delete user
    
        device = devices.query.filter_by(id=device_id).first()
        if device:
            db.session.delete(device)
            db.session.commit()
        else:
            return {'error' : 'no such device found'}, 404
    

# Use the API object to connect the Resource objects to paths on the Flask server
    
# /<datatype: input_name> = a way to have variable paths
api.add_resource(UserAPI, '/device/<int:device_id>')

if __name__ == '__main__':
    app.run(port=8000, debug=True)