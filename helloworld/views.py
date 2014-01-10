from django.shortcuts import render
from helloworld.models import Continent ,Country, Message
from django.http import HttpResponse
# Create your views here.

def welcome(request):
	continents = Continent.objects.all()
	return render(request,"helloworld/welcome.html",{"continents": continents})
	#return HttpResponse("testing welcome")

def continent(request, continent_id):
	continents = Continent.objects.all()
	chosen_continent = Continent.objects.get(pk=continent_id)
	#return HttpResponse("continent %s" % continent_id)
	return render(request,"helloworld/continent.html",{"continent":chosen_continent, "continents": continents})

def country_comment(request,continent_id, country_id):
	continents = Continent.objects.all()
	chosen_country = Country.objects.get(pk=country_id)
	#return HttpResponse("country %s continent %s" % (country_id,continent_id)) 
	return render(request,"helloworld/country_comment.html",{"country":chosen_country, "continents": continents})

def get_message(request,continent_id,country_id):
	chosen_country = Country.objects.get(pk=country_id)
	new_message = Message(author = request.POST["message_author"],
		message = request.POST["message_message"],country = chosen_country)
	return HttpResponseRedirect(reverse('country_comment', args=(continent_id,country_id)))


