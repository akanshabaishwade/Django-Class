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
   

'''