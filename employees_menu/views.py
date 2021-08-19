from datetime import date, datetime
from .models import  Order, Employee, Lunch, Menu
from .forms import OrderForm, MenuForm, LuchForm
from .tasks import send_reminder
from django.http import HttpResponse
from django.shortcuts import render, redirect

def today_menu(request, menu=None):
	context = {}

	try:
		context['menu'] = Menu.objects.get(uuid=menu).lunchs.all()		
	
		return render(request, 'employees_menu/today_menu.html', context)

	except Menu.DoesNotExist:
		return HttpResponse("Menu matching query does not exist")


def new_order(request, lunch=None):
	
	context = {}

	if request.method == 'POST':
		form = OrderForm(request.POST)
		
		if form.is_valid():
			now = datetime.now()
			closed = datetime.now().replace(hour=11, minute=0, second=0, microsecond=0)
			
			if now < closed:
				form.save()
				context['success'] = "Good, your order has been registered"
			else:
				context['message'] = "It is out of business hours"
	else:
		form = OrderForm(initial={'lunch': lunch })
	
	context['form'] = form
	return render(request, 'employees_menu/create_lunch.html', context)


def dashboard(request):
	return render(request, 'employees_menu/dashboard.html')


def menu_index(request):
	
	context = {}

	if request.method == 'POST':

		form = MenuForm(request.POST)

		if form.is_valid():
			new_menu = form.save()			
			#send_reminder(request.build_absolute_uri('/menu/') + str(new_menu.uuid) + "/")
	else:
		form = MenuForm()

	context['menus'] = Menu.objects.all()
	context['form'] = form

	return render(request, 'employees_menu/menus/index.html', context)


def menu_edit(request, menu=None):
	pass

def lunch_index(request):
	context = {}

	if request.method == 'POST':

		form = LuchForm(request.POST, request.FILES)

		if form.is_valid():			
			form.save()
		else:			
			print("Error al guardar")
			print(form.errors)			
	else:
		form = LuchForm()

	context['lunchs'] = Lunch.objects.all()
	context['form'] = form

	return render(request, 'employees_menu/lunchs/index.html', context)
