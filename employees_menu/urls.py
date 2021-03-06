from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'menus'

urlpatterns = [
    path('', views.today_menu, name='today_menu'),
    path('<uuid:menu>/', views.today_menu, name='today_menu'),
    path('new/order/<int:lunch>', views.new_order, name='new_order'),
    path('order/', login_required(views.order_index), name='order_index'),
    path('dashboard/', login_required(views.dashboard), name='dashboard'),
    path('list/', login_required(views.menu_index), name='menu_index'),    
    path('lunch/', login_required(views.lunch_index), name='lunch_index'),    
 ]