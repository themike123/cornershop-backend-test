from datetime import date, datetime
from .models import  Order, Employee, Lunch, Menu
from .forms import OrderForm, MenuForm, LuchForm
from .tasks import send_reminder
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


def today_menu(request, menu=None):
	context = {}
	
	try:
		context['menu'] = Menu.objects.get(uuid=menu).lunchs.all()
	except Menu.DoesNotExist:
		context['menu'] = None

	return render(request, 'employees_menu/today_menu.html', context)

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
			menu = Menu.objects.filter(date=form['date'].value())
			if menu:
				messages.add_message(request, messages.ERROR, 'Menu already exist for this date')
			else:
				new_menu = form.save()
				messages.add_message(request, messages.SUCCESS, 'Luch was saved')				
				send_reminder(request.build_absolute_uri('/menu/') + str(new_menu.uuid) + "/")			
	else:
		form = MenuForm()

	context['menus'] = Menu.objects.all()
	print( Menu.objects.all() )
	context['form'] = form

	return render(request, 'employees_menu/menus/index.html', context)


def lunch_index(request):
	context = {}
	
	if request.method == 'POST':

		form = LuchForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, 'Luch was saved')
	else:
		form = LuchForm()

	context['lunchs'] = Lunch.objects.all()
	context['form'] = form

	return render(request, 'employees_menu/lunchs/index.html', context)

def order_index(request):
	context = {}

	context['orders'] = Order.objects.all()

	return render(request, 'employees_menu/order/index.html', context)
