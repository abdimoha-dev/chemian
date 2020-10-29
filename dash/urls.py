from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name ='login'),
    path('mail',views.mails, name = 'mails'),
    path('adminpage', views.admin_page, name = 'adminpage'),
    path('update', views.update, name = 'update'),
    path('add_main_title', views.add_main, name = 'add_main_title'),
    path('add_about', views.add_about, name = 'add_about'),
    path('add_service', views.add_services, name = 'add_service'),
    path('doctors', views.doctors, name = 'doctors')
    
    
]