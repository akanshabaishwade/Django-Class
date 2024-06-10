'''
Django ORM (Object-Relational Mapping) is a powerful feature of Django that allows you to
 interact with your database using Python objects. It abstracts away the details of SQL queries 
 and provides a simple yet powerful API to perform database operations.

Some important concepts of Django ORM include:

1. **Models**: Models are Python classes that define the structure of your database tables.
 Each model class represents a table, and each attribute of the class represents a field in
   the table. Models are defined in the `models.py` file of your Django app.

2. **QuerySets**: QuerySets are used to retrieve objects from the database. They allow you to 
filter, update, and delete objects using simple Python code. QuerySets are lazily evaluated,
 meaning the database query is not executed until the results are actually needed.

3. **Field Types**: Django provides a variety of field types (e.g., `CharField`, `IntegerField`,
 `DateTimeField`, etc.) to define the type of data stored in each field of a model. These field 
 types map to corresponding database column types.

4. **Queries**: Django provides a rich API for querying the database using QuerySets. You can filter,
 exclude, annotate, aggregate, and perform other operations on QuerySets to retrieve the data you need.

5. **Relationships**: Django supports different types of relationships between models, 
such as `ForeignKey`, `ManyToManyField`, and `OneToOneField`, to represent the relationships 
between different tables in your database.

6. **Migrations**: Migrations are Django's way of propagating changes you make to your models
 (adding a field, deleting a model, etc.) into your database schema. Django generates migration files that contain Python code to apply these changes to the database schema.

7. **Transactions**: Django supports database transactions to ensure the integrity of your data. 
You can use the `transaction.atomic` decorator or context manager to wrap your database operations
 in a transaction.

8. **Aggregation**: Django provides aggregation functions like `Sum`, `Count`, `Avg`, etc., 
to perform aggregate calculations on QuerySets.

9. **Model Managers**: Model managers are used to encapsulate the logic for querying the database.
 You can define custom model managers to add custom query methods to your models.

10. **Signals**: Signals allow certain senders to notify a set of receivers when certain 
actions have taken place. In Django, signals are used to decouple the logic of different parts 
of your application.

These are some of the important concepts of Django ORM. Understanding these concepts will 
help you effectively work with databases in your Django projects.
'''


'''

from appname.models import *

model_names = ModelName.objects.all()
model_names = ModelName.objects.all().first()
ModelName.objects.create(field1='Sample Field 1', field2='Sample Field 2')
Student.objects.filter(age=21) 
Student.objects.get(first_name='Alice')

# Get a specific record
student_alice = Student.objects.get(first_name='Alice')
print("Student named Alice:", student_alice)

# Updating a record
student_alice.age = 21
student_alice.save()
print("Updated student:", Student.objects.get(first_name='Alice'))

# Update using QuerySet's update method
Student.objects.filter(first_name='Alice').update(age=21)
print("Updated student:", Student.objects.get(first_name='Alice'))

# Deleting a record
student_alice.delete()
print("All students after deletion:", Student.objects.all())
exit()
'''