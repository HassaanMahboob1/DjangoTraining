from curses.ascii import HT
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.

def index(request):
    return render(request, 'polls/index.html')
    # return HttpResponse("Hello, world. You are the polls index.")

def detail(request,question_id):
    return HttpResponse("You are looking at response %s ." % question_id)

def results (request,question_id):
    return HttpResponse("You are looking at the results of the question %s ." % question_id)

def vote (request , questions_id):
    return HttpResponse("You are voting at the question %s ." % questions_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)