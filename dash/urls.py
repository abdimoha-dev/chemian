from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='chemian'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('book_consultation',views.book_consultation, name = 'book_consultation'),
    path('adminpage', views.admin_page, name = 'adminpage'),
    path('update', views.update, name = 'update'),
    path('add_main_title', views.add_main, name = 'add_main_title'),
    path('add_about', views.add_about, name = 'add_about'),
    path('add_service', views.add_services, name = 'add_service'),
    path('doctors', views.doctors, name = 'doctors'),
    path('physical_app', views.physical_app, name = 'physical_app')
       
]