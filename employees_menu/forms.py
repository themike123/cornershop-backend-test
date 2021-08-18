from django import forms
from .models import Lunch, Order, Employee, Menu
from django.forms import ModelForm, Select, Textarea, DateField, DateInput

#from employees_menu.validators import validate_create_order_before_to_11am

class LuchForm(ModelForm):
    class Meta:
        model = Lunch
        fields = ['name', 'photo', 'description']
        widgets = {            
            'description': Textarea(attrs={
                'class': "form-control",
                'style': 'max-height: 100px;',                
                }),
        }

class OrderForm(ModelForm):    

    class Meta:
        model = Order
        fields = ['lunch', 'employee', 'note']
        widgets = {
            'lunch': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',                
                }),
            'employee': Select(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',            
                }),
            'note': Textarea(attrs={
                'class': "form-control",
                'style': 'max-height: 100px;',            
                'placeholder': 'Notes for the lunch'
                })
        }

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'last_name']

class MenuForm(ModelForm):

    #date = forms.DateField(initial=date.today(), validators=[validate_create_order_before_to_11am])    

    class Meta:
        model = Menu
        fields = ['lunchs', 'date']
        widgets = {            
            'date': DateInput(attrs={
                'type': 'date',
                'style': "form-control",
                }),
        }