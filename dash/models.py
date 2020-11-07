from django.db import models
import datetime
from dashboard import  settings


class Title(models.Model):
    def __str__(self):
        return self.main_title
    
    main_title = models.CharField(max_length=50)
    main_body = models.CharField(max_length=500)
    main_image = models.ImageField(upload_to ='images', null=True, blank =True)
    
class About(models.Model):
    def __str__(self):
        return self.about_title

    about_title = models.CharField(max_length=50, null=True)
    about_body = models.CharField(max_length=500, null=True)
    
class Service(models.Model):
    service_title = models.CharField(max_length=50, null=True)
    service_description = models.CharField(max_length=500, null=True)
    
class Doctor(models.Model):
    doctor_name = models.CharField(max_length=50, null=True)
    doctor_specialization = models.CharField(max_length=50, null=True)
    doctor_details = models.CharField(max_length=500, null=True)
    doctor_photo = models.ImageField(upload_to ="images", null=True)
    
class P_Appointment(models.Model):
    full_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    date = models.DateField(null=False)
    time = models.TimeField(null=False)
    message = models.CharField(max_length=50, null=True)
   
class Online_appointments(models.Model):
    full_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    details = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to ="images", null=True)
    
class Service_image(models.Model):
    service_image = models.ImageField(upload_to ='images', null=True, blank =True)
    
class Testimonial(models.Model):
    name = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    testimonial = models.CharField(max_length=500, null=True)
    photo = models.ImageField(upload_to ='images', null=True, blank =True)
    