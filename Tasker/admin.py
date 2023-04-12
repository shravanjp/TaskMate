from django.contrib import admin
from .models import Category, ToDoList

admin.site.register(ToDoList)
admin.site.register(Category)