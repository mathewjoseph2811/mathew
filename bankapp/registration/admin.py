from django.contrib import admin
from .models import register, District, Branch

# Register your models here.
admin.site.register(register)
admin.site.register(District)
admin.site.register(Branch)