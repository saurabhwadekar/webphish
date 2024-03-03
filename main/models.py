from django.db import models
# Create your models here.

class Target(models.Model):
    url = models.CharField("url",max_length=1000)
    redirect_url = models.CharField("Redirect Url",null=True,blank=True,max_length=1000)
    form_id= models.CharField("Form ID",null=True,blank=True,max_length=100)
    btn_id= models.CharField("Button ID",null=True,blank=True,max_length=100)
    username_id_name= models.CharField("Username Field ID Or Name",null=True,blank=True,max_length=100)
    password_id_name= models.CharField("Password Filed ID Or Name",null=True,blank=True,max_length=100)
    date_time = models.DateTimeField(auto_now=True)


class Data(models.Model):
    url = models.CharField("url",max_length=1000)
    data = models.TextField("data")
    ip = models.CharField("ip Address",max_length=1000)
    date_time = models.DateTimeField(auto_now=True)