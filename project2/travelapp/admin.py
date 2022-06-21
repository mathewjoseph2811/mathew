from django.contrib import admin

# Register your models here.
from . models import travel, person

admin.site.register(travel)
admin.site.register(person)