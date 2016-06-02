from django.shortcuts import render

from django.http import HttpResponse

#Importing our fact model into the views

#Imports EVERYTHING in models.py
##from facts import models

##Cleaner -- imports only the class we are after (just so happens we only have 1!)
from facts.models import Fact
import random

# Create your views here.
def getFact(request):
	import pdb
	#pdb.set_trace()
	return HttpResponse(Fact.objects.get(id=random.randint(1,Fact.objects.count())))
