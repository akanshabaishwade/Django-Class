'''
1. Resolving Unapplied Migrations Error:
   - You have 18 unapplied migration(s), indicating changes to your models that haven't been applied 
   to your database.
   - To apply these migrations, run:
     python manage.py migrate

2. Resolving Port Already in Use Error:
   - The error "That port is already in use" means that the port your Django development server
     (run with python manage.py runserver) is trying to use is already being used by another process.
   - To resolve this, you can either:
     - Stop the process using the port (if it's not needed) and restart your Django development
       server, or
     - Specify a different port for your Django development server using the --port option, like so:
       python manage.py runserver 8000 or new port (ex. 9000)
       python manage.py runserver 9000

3. Introduction to Models:
   - Models in Django are Python classes that define the structure of your application's data.
   - They are used to create database tables and manage interactions with the database.

admin-panel  -
python manage.py createsuperuser
Username (leave blank to use 'akansha'): admin
Email address: 
Password: 
Password (again): 
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
http://127.0.0.1:8000/admin/


4. Why We Create Models:
   - Models help us represent real-world objects in our application.
   - They allow us to define the attributes and behavior of these objects.
   - Models enable us to store and retrieve data from the database in a structured way.


'''
