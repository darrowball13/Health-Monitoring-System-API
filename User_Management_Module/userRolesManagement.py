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
roles_table_connect = sqlite3.connect("roles.db")

roles_cur = roles_table_connect.cursor()

roles_cur.execute('''
CREATE TABLE IF NOT EXISTS roles (
  id integer PRIMARY KEY,
  user_id integer
  role_type varchar(255),
  time_added timestamp
)''')

roles_table_connect.commit()

roles_table_connect.close()

# Configure the app to connect to the database 'users.db' SQLite file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'roles.db')
db = SQLAlchemy(app)

# Define the SQLite table schema (with the same name) as a db.Model object
class roles(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, nullable = False)
    role_type = db.Column(db.String(255), nullable = False)
    time_added = db.Column(db.DateTime(timezone=True), server_default= func.now())

    def __init__(self, id, user_id, role_type, time_added):
        self.id = id
        self.user_id = user_id
        self.role_type = role_type
        self.time_added = time_added

    # Shows what values are returned when this object is queried
    def __repr__(self):
        return self.name

# Define output data schema
role_definition = {
    'role_id' : fields.Integer,
    'user_id' : fields.Integer,
    'role_type' : fields.String
}

class FormatRole(object):
    def __init__(self, id, user_id, role_type):
        self.role_id = id
        self.user_id = user_id
        self.role_type = role_type


# Define request parser
parser = reqparse.RequestParser()
parser.add_argument('first_name', help="First Name cannot be blank")
parser.add_argument('last_name', help="Last Name cannot be blank")

# get_user uses SQLAlchemy rather than the users dict
def get_role(role_id):
    # If find role, return
    role = role.query.filter_by(id=role_id).first()

    try:
        if (role):
            return FormatRole(role.id, role.type)
        # Otherwise, send error message and error code
        else:
            return {'error' : 'User not found'}, 404
    except Exception as e:
        print(e)

# Define a Resource-type class object to define functions for the RESTful API
class RoleAPI(Resource):

    # GET function
    # marshal_with will serialize the API response to follow schema
    @marshal_with(role_definition)
    def get(self, role_id):
        return get_role(role_id)
    
    # PUT / POST function
    @marshal_with(role_definition)
    def post(self, role_id):

        # Parse request for desired values name and secret
        try:
            args = parser.parse_args()

            # NEW: Start SQLite db session, insert and commit
            new_role = roles(role_id, args['user_id'], args['role_type'], args['time_added'])
            db.session.add(new_role)
            db.session.commit()

            return FormatRole(role_id, args['role_type'])
        except Exception as e:
            print(e)
            return e

    # DELETE function for deleting resources from the API
    def delete(self, role_id):

        # NEW: Use db session to find and delete user
        try:
            role = roles.query.filter_by(id=role_id).first()
            if (role):
                db.session.delete(role)
                db.session.commit()
            else:
                return {'error' : 'User not found'}, 404
        except Exception as e:
            return e
    

# Use the API object to connect the Resource objects to paths on the Flask server
# Once running the app, can test that it's working: curl http://127.0.0.1:5000
# Example PUT curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
    
# /<datatype: input_name> = a way to have variable paths
api.add_resource(RoleAPI, '/roles /<int:role_id>')

if __name__ == '__main__':
    app.run(port=8000, debug=True)