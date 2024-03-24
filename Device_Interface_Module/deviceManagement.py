from flask import Flask, jsonify, request
from flask_restful import Resource, Api, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import sqlite3
import os


# Aspects of this were adapted from following page:
# https://github.com/TrevorChan1/EC530-flaskrestful-demo/blob/main/3.%20demo_with_database/app.py

# Define flask app and flask_restful API objects
app = Flask(__name__)
api = Api(app)

# Create user.db table if it doesn't already exist. Source: https://docs.python.org/3/library/sqlite3.html
device_table_connect = sqlite3.connect("devices.db")

device_cur = device_table_connect.cursor()

device_cur.execute('''
CREATE TABLE IF NOT EXISTS devices (
  id integer PRIMARY KEY,
  device_type varchar(255),
  time_added timestamp
)''')

device_table_connect.commit()

device_table_connect.close()

# Configure the app to connect to the database 'users.db' SQLite file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'devices.db')
db = SQLAlchemy(app)

# Define the SQLite table schema (with the same name) as a db.Model object
class devices(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    device_type = db.Column(db.String(255), nullable = False)
    time_added = db.Column(db.DateTime(timezone=True), server_default= func.now())

    def __init__(self, id, device_type, time_added):
        self.id = id
        self.device_type = device_type
        self.time_added = time_added

    # Shows what values are returned when this object is queried
    def __repr__(self):
        return self.name

# Define output data schema
device_definition = {
    'device_id' : fields.Integer,
    'device_type' : fields.String
}

class FormatDevice(object):
    def __init__(self, id, device_type):
        self.device_id = id
        self.device_type = device_type


# Define request parser
parser = reqparse.RequestParser()
parser.add_argument('device_type', help="Device type cannot be blank")

# get_user uses SQLAlchemy rather than the users dict
def get_device(device_id):
    # If find user, return
    device = device.query.filter_by(id=device_id).first()

    try:
        if (device):
            return FormatDevice(device.id, device.type)
        # Otherwise, send error message and error code
        else:
            return {'error' : 'User not found'}, 404
    except Exception as e:
        print(e)

# Define a Resource-type class object to define functions for the RESTful API
class DeviceAPI(Resource):

    # GET function
    # marshal_with will serialize the API response to follow schema
    @marshal_with(device_definition)
    def get(self, device_id):
        return get_device(device_id)
    
    # PUT / POST function
    @marshal_with(device_definition)
    def post(self, device_id):

        # Parse request for desired values name and secret
        try:
            args = parser.parse_args()

            # NEW: Start SQLite db session, insert and commit
            new_device = devices(device_id, args['device_type'], args['time_added'])
            db.session.add(new_device)
            db.session.commit()

            return FormatDevice(device_id, args['device_type'])
        except Exception as e:
            print(e)
            return e

    # DELETE function for deleting resources from the API
    def delete(self, user_id):

        # NEW: Use db session to find and delete user
        try:
            device = devices.query.filter_by(id=user_id).first()
            if (device):
                db.session.delete(device)
                db.session.commit()
            else:
                return {'error' : 'User not found'}, 404
        except Exception as e:
            return e
    

# Use the API object to connect the Resource objects to paths on the Flask server
# Once running the app, can test that it's working: curl http://127.0.0.1:5000
# Example PUT curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
    
# /<datatype: input_name> = a way to have variable paths
api.add_resource(DeviceAPI, '/device /<int:device_id>')

if __name__ == '__main__':
    app.run(port=8000, debug=True)