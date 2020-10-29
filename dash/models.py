from django.db import models

class Title(models.Model):
    def __str__(self):
        return self.main_title
    
    main_title = models.CharField(max_length=50)
    main_body = models.CharField(max_length=500)
    main_image = models.ImageField(upload_to ='dash/images', null=True)
    
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
    doctor_photo = models.ImageField(upload_to ='images', null=True)