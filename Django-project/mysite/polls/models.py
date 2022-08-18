import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    entrydate = models.CharField(max_length=200,default='')
   

    def __str__(self) :
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    choice_text  = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)    


    def __str__(self):
        return self.choice_text

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)      
    Age = models.IntegerField(default=0)  