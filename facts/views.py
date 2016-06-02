from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def hello(request, name="dawg"):
	import pdb
	#pdb.set_trace()
	return HttpResponse("Yo %s!" %name) 
