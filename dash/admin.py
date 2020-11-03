from django.contrib import admin
from .models import Title,Service, Doctor,P_Appointment,Online_appointments

admin.site.register(Title)
admin.site.register(Service)
admin.site.register(Doctor)
admin.site.register(P_Appointment)
admin.site.register(Online_appointments)
