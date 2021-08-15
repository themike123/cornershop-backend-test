import uuid
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Menu(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/lunch')
    date = models.DateField()
    description = models.TextField()

class Order(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateTimeField(editable=False, auto_now_add=True)