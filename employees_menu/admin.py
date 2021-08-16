from django.contrib import admin

from .models import Menu
from .models import Employee
from .models import Order

admin.site.register(Menu)
admin.site.register(Employee)
admin.site.register(Order)
