from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.OneToOneField(Publisher, on_delete=models.SET_NULL, null=True, blank=True)
    readers = models.ManyToManyField('Reader', through='Reading', related_name='books')

    def __str__(self):
        return self.title

class Reader(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Reading(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_started = models.DateField()
    date_finished = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.reader.name} is reading {self.book.title}"


class BookReader(models.Model):
    title = models.CharField(max_length=200)
    readers = models.ManyToManyField(Reader)


    def __str__(self):
        return self.title