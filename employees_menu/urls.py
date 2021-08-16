from django.urls import path
from . import views

app_name = 'menus'

urlpatterns = [
    path('menu/<uuid:employee>', views.menu, name='choice_menu'),
    path('panel', views.panel, name='index'),
    path('menus', views.list_menus, name='list_menus'),
    path('orders', views.list_orders, name='list_orders'),
]