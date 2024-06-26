from django.contrib import admin
from .models import *
# Register your models here.

# Register the Student model with the admin interface
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('first_name', 'last_name', 'age', 'date_of_birth')

    # Enable filtering by age and date_of_birth in the admin panel
    list_filter = ('age', 'date_of_birth')

    # Enable search functionality by first_name and last_name
    search_fields = ('first_name', 'last_name')

    # Define the fields layout in the add/change form
    # fields = ('first_name', 'last_name', 'age', 'date_of_birth')

    # Optionally, define fieldsets for a more organized form layout
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name')
        }),
        ('Additional Info', {
            'fields': ('age', 'date_of_birth'),
            'classes': ('collapse',)  # Collapsible section
        }),
    )
'''
Explanation:
@admin.register(Student): This decorator registers the Student model with the admin site and associates 
it with the StudentAdmin class.
list_display: Specifies the fields to display in the admin list view of Student instances.
list_filter: Enables filtering by age and date_of_birth in the admin panel sidebar.
search_fields: Enables searching by first_name and last_name using a search box.
fields: Specifies the order and which fields appear in the add/change form for Student.
fieldsets: Allows you to group fields in sections in the add/change form, providing a more organized layout.
'''
# admin.site.register(Student)
admin.site.register(ModelName)
admin.site.register(AllFieldType)

