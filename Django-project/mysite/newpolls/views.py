from curses import beep
from django.shortcuts import render
from django.http import HttpResponse
from .models import Betting
from .forms import BettingForm, forms

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
# Create your views here.

def new_index(request):
    return HttpResponse("You are in new polls project")

 
def create_view(request):
    context ={}
    form = BettingForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_view.html", context)    


def list_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["dataset"] = Betting.objects.all()
		
	return render(request, "list_view.html", context)

def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Betting, id = id)
    print("my object is : " , obj)
    # pass the object as instance in form
    form = BettingForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)