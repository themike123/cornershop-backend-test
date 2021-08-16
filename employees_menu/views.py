from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Menu, Order, Employee
from datetime import date
from .forms import OrderForm

def menu(request, employee=None):
	if request.method == 'POST':
		print(request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()			
			#return redirect()
		else:
			print("Error al guardar")
			print(form.errors)
	else:
		pass		

	form = OrderForm(initial={'employee': employee })
	data = {'menus': Menu.objects.filter(date=date.today()),
			'form': form}

	return render(request, 'employees_menu/choice_menu.html', data)


def panel(request):
	return render(request, 'employees_menu/panel.html')

def list_menus(request):
	return render(request, 'employees_menu/list_menus.html')

def list_orders(request):
	return render(request, 'employees_menu/list_orders.html')


