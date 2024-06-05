'''
orm 
data = ModelName.objects.filter()
print(data)




5. Field Types:
   - Django provides various field types that correspond to different data types in the database.
   - Common field types include CharField, IntegerField, BooleanField, DateField, DateTimeField, 
   ForeignKey, ManyToManyField, etc.
   - https://docs.djangoproject.com/en/5.0/ref/models/fields/

6. Example:
   - Here's an example of creating a simple Django model for a Student table with a few fields:
     from django.db import models

     class Student(models.Model):
         first_name = models.CharField(max_length=100)
         last_name = models.CharField(max_length=100)
         age = models.IntegerField()
         date_of_birth = models.DateField()
         
7. Interacting with Databases:

* Interacting with databases in Django can be done in two main ways: the "dumb way" and the "MTV way"
 (Model-Template-View way).

* The "dumb way" refers to directly writing SQL queries in your views or other parts of your
 code to interact with the database. This approach is discouraged in Django as it bypasses Django's
   ORM and can lead to low security and code that is difficult to maintain.
* The "MTV way" involves using Django's ORM (Object-Relational Mapping) to interact with the database. 
This approach is recommended as it abstracts away the details of the database and allows you to work with 
Python objects instead of raw SQL.

'''