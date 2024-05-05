# Health-Monitoring-System-API

This repository holds the code for a simple healthcare app developed for the course EC530 Software Engineering Foundations. It is a Python-based application, and was created with Python 3.12.2 installed

## Requirements

In the main directory, there is a text file "requirements.txt" that contains all of the requirements needed for this app. In order to install these requirements, open a terminal from the main directory and run the following command:

> pip install -r requirements.txt

## Usage

Before starting the main app, there is a RESTFUL API that needs to be started from within the User_Management_Module folder: "userManagement.py". This API contains GET, POST, and DELETE requests for the table _users_ from within the database "users.db". Additionally, if the table or database does not exist, starting the Python file above will create these as well. Therefore, begin by open a terminal from the User_Management_Module folder and run the following command:

> python userManagement.py

If this runs properly, the terminal should display the following (Note that it is in debug mode):

<p align="center">
  <img src = "https://github.com/darrowball13/Health-Monitoring-System-API/assets/113733798/44fffb64-6c51-4513-a040-18f48590157f" />
</p>

Once the userManagement API is up and running, the file "DarrowHealthApp.py" is the main file that starts the app. To start the main app, the following command must be run in a terminal:

> python DarrowHealthApp.py

This opens the main application, which prompts the user for the following:
<p align="center">
  <img src = "https://github.com/darrowball13/Health-Monitoring-System-API/assets/113733798/66f4ff6c-29e8-4fd3-9939-91b5ff5321db" />
</p>

Commands must then be entered into the terminal based on available commands from the given menu. The database given in this respository should have some records for a variety of different user types, but a new user profile may be created by selecting the **Register** option.
