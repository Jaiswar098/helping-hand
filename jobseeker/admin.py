from django.contrib import admin
from .models import Person
# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    '''Admin View for Person'''

    list_display = ('name', 'email', 'phone', 'city',
                    'state', 'pincode', 'education',
                     'created_on', 
                    'updated_on')