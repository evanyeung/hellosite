from django.shortcuts import render
from helloworld.models import Continent ,Country, Message
from django.http import HttpResponse
# Create your views here.

def welcome(request):
	return render(request,"helloworld/welcome.html",{})
	#return HttpResponse("testing welcome")

def continent(request, continent_id):
	chosen_continent = Continent.objects.get(pk=continent_id)
	#return HttpResponse("continent %s" % continent_id)
	return render(request,"helloworld/continent.html",{"continent":chosen_continent})

def country_comment(request,continent_id, country_id):
	chosen_country = Country.objects.get(pk=country_id)
	#return HttpResponse("country %s continent %s" % (country_id,continent_id)) 
	return render(request,"helloworld/country_comment.html",{"country":chosen_country})

def message(request):
	
