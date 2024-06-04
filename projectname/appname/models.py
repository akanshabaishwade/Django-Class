from django.db import models



class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField() #123
    date_of_birth = models.DateField()


class ModelName(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=50, blank=True, null=True, help_text="enter name of field")


















# class AllFieldType(models.Model):
#     # AutoField: It automatically increments.
#     auto_field = models.AutoField(primary_key=True)  # Example: auto_field=1
    
#     # BigAutoField: 64-bit integer guaranteed to fit numbers from 1 to 9223372036854775807.
#     big_auto_field = models.BigAutoField()  # Example: big_auto_field=9223372036854775807
    
#     # BigIntegerField: 64-bit integer guaranteed to fit numbers from -9223372036854775808 to 9223372036854775807.
#     big_integer_field = models.BigIntegerField()  # Example: big_integer_field=-9223372036854775808
    
#     # BinaryField: Field to store raw binary data.
#     binary_field = models.BinaryField()  # Example: binary_field=b'\x01\x02\x03'
    
#     # BooleanField: True/false field. Default form widget is CheckboxInput.
#     boolean_field = models.BooleanField()  # Example: boolean_field=True
    
#     # CharField: Field to store text-based values.
#     char_field = models.CharField(max_length=255)  # Example: char_field='example text'
    
#     # DateField: Date, represented in Python by a datetime.date instance.
#     date_field = models.DateField()  # Example: date_field='2022-06-01'
    
#     # DateTimeField: Date and time, represented in Python by a datetime.datetime instance.
#     date_time_field = models.DateTimeField()  # Example: date_time_field='2022-06-01T12:00:00'
    
#     # DecimalField: Fixed-precision decimal number, represented in Python by a Decimal instance.
#     decimal_field = models.DecimalField(max_digits=10, decimal_places=2)  # Example: decimal_field=1234.56
    
#     # DurationField: Field for storing periods of time.
#     duration_field = models.DurationField()  # Example: duration_field='2 days, 3:00:00'
    
#     # EmailField: CharField that checks that the value is a valid email address.
#     email_field = models.EmailField()  # Example: email_field='user@example.com'
    
#     # FileField: File-upload field.
#     file_field = models.FileField(upload_to='uploads/')  # Example: file_field='path/to/file.txt'
    
#     # FloatField: Floating-point number, represented in Python by a float instance.
#     float_field = models.FloatField()  # Example: float_field=3.14
    
#     # ImageField: Inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
#     image_field = models.ImageField(upload_to='images/')  # Example: image_field='path/to/image.jpg'
    
#     # IntegerField: Integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.
#     integer_field = models.IntegerField()  # Example: integer_field=42
    
#     # GenericIPAddressField: IPv4 or IPv6 address, in string format.
#     generic_ip_address_field = models.GenericIPAddressField()  # Example: generic_ip_address_field='192.0.2.1'
    
#     # NullBooleanField: Like a BooleanField, but allows NULL as one of the options.
#     null_boolean_field = models.NullBooleanField()  # Example: null_boolean_field=True
    
#     # PositiveIntegerField: Like an IntegerField, but must be either positive or zero (0).
#     positive_integer_field = models.PositiveIntegerField()  # Example: positive_integer_field=123
    
#     # PositiveSmallIntegerField: Like a PositiveIntegerField, but only allows values under a certain (database-dependent) point.
#     positive_small_integer_field = models.PositiveSmallIntegerField()  # Example: positive_small_integer_field=5
    
#     # SlugField: A short label for something, containing only letters, numbers, underscores, or hyphens. Generally used in URLs.
#     slug_field = models.SlugField()  # Example: slug_field='example-slug'
    
#     # SmallIntegerField: Like an IntegerField, but only allows values under a certain (database-dependent) point.
#     small_integer_field = models.SmallIntegerField()  # Example: small_integer_field=10
    
#     # TextField: Large text field. Default form widget is Textarea.
#     text_field = models.TextField()  # Example: text_field='large text content'
    
#     # TimeField: Time, represented in Python by a datetime.time instance.
#     time_field = models.TimeField()  # Example: time_field='12:00:00'
    
#     # URLField: CharField for a URL, validated by URLValidator.
#     url_field = models.URLField()  # Example: url_field='https://www.example.com'
    
#     # UUIDField: Field for storing universally unique identifiers.
#     uuid_field = models.UUIDField()  # Example: uuid_field='550e8400-e29b-41d4-a716-446655440000'

#     def __str__(self):
#         return f'MyModel object ({self.auto_field})'
