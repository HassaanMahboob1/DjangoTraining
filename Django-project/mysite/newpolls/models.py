from email.policy import default
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)      
    Age = models.IntegerField(default=0)  

    def __str__(self):
        return self.first_name

class Betting(models.Model):
    Betting_id  = models.IntegerField(default=0)
    Betting_amount = models.IntegerField(default = 0)
    Upload_Image = models.ImageField(upload_to = "images/",default='')

    def __str__(self):
        return (f"{self.Betting_id}")