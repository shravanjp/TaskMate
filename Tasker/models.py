from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name : models.CharField(max_length = 100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class ToDoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created_time = models.DateField(default=timezone.now().strftime("%d-%m-%y")) 
    due_time = models.DateField(default=timezone.now().strftime("%d-%m-%y")) 
    category = models.ForeignKey(Category,default="general",on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.title


