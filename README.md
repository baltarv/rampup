# Description 

This project give an example of how to use Django and Django Rest Framework to create RESTFult API's.

## How to run the projec. 

### First step. 
- Create your virtual environment 
- [SUGGESTION]In the root folder of the project runs.
    - python3.8 -m venv venv

### PS: 
    Please note the python version used for this project. 

### Second step. 
- Install dependencies.
- in the root folder run: 
     `pip install -r requirements.txt`
- make sure your virtual environment is active. 

### Third step. 
- run migrations. 
    `python manage.py migrate`

### Fourth step. 
- run the initial load for the db. for that we should run two management commands. 
    first: `python manage.py loag_packages_channels`
    second: `python manage.py load_package_map`

### Fith step.
- run `python manage.py runserver` to start the server. 
- access localhost:8000/docs to see the API documentation.