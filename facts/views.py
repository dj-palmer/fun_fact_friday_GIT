import random

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#Importing our fact model into the views

#Imports EVERYTHING in models.py
##from facts import models

##Cleaner -- imports only the class we are after (just so happens we only have 1!)
from facts.models import Fact

# Create your views here.
def getFact(request):
	import pdb
	#pdb.set_trace()
	fact=Fact.objects.get(id=random.randint(1,Fact.objects.count()))
	template = loader.get_template('facts/index.html')
	context = {"fact" : fact}
	return HttpResponse(template.render(context,request))

def getFacts(request):
	facts=Fact.objects.all()
	template = loader.get_template('facts/facts.html')
	context = {"facts" : facts}
	return HttpResponse(template.render(context,request))

