from django.shortcuts import render

def menu(request):
	return render(request, 'employees_menu/choice_menu.html')

def panel(request):
	return render(request, 'employees_menu/panel.html')

def list_menus(request):
	return render(request, 'employees_menu/list_menus.html')

def list_orders(request):
	return render(request, 'employees_menu/list_orders.html')


