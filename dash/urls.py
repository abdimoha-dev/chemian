from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mail',views.mails, name = 'mails'),
    path('adminpage', views.admin_page, name = 'adminpage'),
    path('update', views.update, name = 'update')
]