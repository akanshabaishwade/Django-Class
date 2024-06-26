from django.contrib import admin
from .models import Author, Publisher, Book, Reader, Reading, BookReader


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher')
    list_filter = ('author', 'publisher')
    search_fields = ('title', 'author__name', 'publisher__name')

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ('reader', 'book', 'date_started', 'date_finished')
    list_filter = ('date_started', 'date_finished')
    search_fields = ('reader__name', 'book__title')
    
    
admin.site.register(BookReader)


