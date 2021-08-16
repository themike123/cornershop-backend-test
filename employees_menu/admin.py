from django.contrib import admin

from .models import Employee
from .models import Order
from .models import Lunch
from .models import Menu

admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Lunch)
admin.site.register(Menu)
