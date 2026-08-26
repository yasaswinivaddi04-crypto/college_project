College Management System

A Django-based web application for managing college student and department information. The project provides an easy-to-use interface for adding, viewing, updating, and managing student and department records.

Features

- Student management
- Department management
- Add, view, update, and delete records
- Django Admin interface
- Dynamic HTML templates
- SQLite database for development
- Organized Django app structure

Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Git & GitHub

Project Structure

college_project/
│
├── college_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── studentApp/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── manage.py
├── .gitignore
└── README.md

Installation

1. Clone the repository

git clone https://github.com/yasaswinivaddi04-crypto/college_project.git

2. Open the project

cd college_project

3. Create a virtual environment

python -m venv my_env

4. Activate the virtual environment

Windows:

my_env\Scripts\activate

5. Install Django

pip install django

6. Apply migrations

python manage.py migrate

7. Start the development server

python manage.py runserver

Open the application in your browser:

http://127.0.0.1:8000/

Django Admin

To create an administrator account:

python manage.py createsuperuser

Then visit:

http://127.0.0.1:8000/admin/

Database

The project uses SQLite during development.

The database file ("db.sqlite3") is excluded from Git using ".gitignore".

GitHub

Repository:

https://github.com/yasaswinivaddi04-crypto/college_project

Future Improvements

- Add user authentication
- Add student search and filtering
- Improve UI with Bootstrap or Tailwind CSS
- Add PostgreSQL support
- Add REST API functionality
- Deploy the application online

License

This project is intended for educational and learning purposes.