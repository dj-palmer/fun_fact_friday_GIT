import random

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Importing our fact model into the views

# Imports EVERYTHING in models.py
# from facts import models

# Cleaner -- imports only the class we are after
from facts.models import Fact


def getFact(request):
    fact = Fact.objects.get(id=random.randint(1, Fact.objects.count()))
    template = loader.get_template('facts/index.html')
    context = {"fact": fact}
    return HttpResponse(template.render(context, request))


def getFacts(request):
    facts = Fact.objects.all()
    template = loader.get_template('facts/facts.html')
    context = {"facts": facts}
    return HttpResponse(template.render(context, request))
