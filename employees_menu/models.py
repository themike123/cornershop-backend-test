import uuid
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100, blank=True) 

class Lunch(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='uploads/lunch')
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Menu(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lunchs = models.ManyToManyField(Lunch)
    date = models.DateField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.date

class Order(models.Model):
    lunch = models.ForeignKey(Lunch, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    note = models.TextField(blank=True)
    date = models.DateTimeField(editable=False, auto_now_add=True)
