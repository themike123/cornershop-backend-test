from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'menus'

urlpatterns = [
    path('', views.today_menu, name='today_menu'),
    path('<uuid:menu>/', views.today_menu, name='today_menu'),
    path('new/order/<int:lunch>', views.new_order, name='new_order'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('list/', views.menu_index, name='menu_index'),
    path('new/', views.menu_new, name='menu_new'),
    path('edit/<int:menu>', views.menu_edit, name='menu_edit'),
    path('lunch/', views.lunch_index, name='lunch_index'),
    path('lunch/new/', views.lunch_new, name='lunch_new'),    
 ]