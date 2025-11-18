# Create Django-Project: 
- Create a virtual environment `python -m venv env`
- add a file called `.gitignore` then add the relative path of the env file inside it
- activate the environment:
    - linux: source `env/bin/activate`
    - windows: `.\env\Scripts\activate`
- install django: `pip install Django` (environment variables must be active)
- create project: `django-admin startproject projectFlow` (projectFlow is just a name it can be anything)
- change the directory(cd) to the projectFlow then check whether in that directory you have the `manage.py` file :  `cd projectFlow`
- run the project: `python manage.py runserver`