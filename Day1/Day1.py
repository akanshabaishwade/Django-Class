'''
python -m venv venv_name: Creates a new Python virtual environment named venv_name.

pip install Django==5.0.6: Installs Django version 5.0.6 into the virtual environment.

django-admin startproject myproject: Creates a new Django project named myproject.

django-admin startapp myapp: Creates a new Django app named myapp within the project.
'''

'''
Project 

command - django-admin startproject myproject

1. In Django, a project is a collection of settings for an instance of Django,
   including database configuration, Django-specific options, and application-specific settings.
   It represents a complete web application.

2. settings.py

3. A project is typically the top-level directory that contains all the files and directories needed 
   for a Django application to run.

4. a project's default file names include settings.py (for project settings), urls.py (for URL patterns),
 wsgi.py (for WSGI deployment), asgi.py (for ASGI deployment), manage.py (for project management)

'''

'''
App

command - django-admin startapp myapp 

1. In a Django app, the default file names include init.py (for package recognition),
 models.py (for database models), views.py (for view functions), 
 admin.py (for admin interface registration), and apps.py (for app configuration), tests.py.

'''
