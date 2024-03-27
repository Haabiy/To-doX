from django.contrib import admin

# Register your models here.
from . models import todo, Profile

admin.site.register(todo)
admin.site.register(Profile)
