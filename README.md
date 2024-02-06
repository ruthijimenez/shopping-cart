# Creation of shopping-cart microservice

## Setup the Project Directory:
* Create a project directory and navigate to it in your terminal.

## Initialize a Virtual Environment:
python3 -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"

## Install Required Packages (Install Flask and SQLAlchemy)
pip install Flask
pip install Flask-SQLAlchemy

## Create the Project Structure:
shopping-cart/
├── app.py
├── models.py
├── database.py
├── routes.py
└── venv/

## Write py file:
* Define the Database Models (models.py):
* Initialize the Flask App (app.py):
* Create Database Configuration (database.py):
* Create Routes (routes.py):

## Run the Application with script:
chmod +x deploy.sh
./deploy.sh

## To run without script and minikube
python app.py

Your shopping cart microservice should now be running: http://localhost:5000

## Testing and Further Development:
You can use tools like curl or Postman to test the endpoints defined in routes.py. Additionally, you can expand the functionality to handle adding, updating, and removing items from the cart as per your requirements.
