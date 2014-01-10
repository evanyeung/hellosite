from django.shortcuts import render,get_object_or_404
from helloworld.models import Continent ,Country, Message
from django.http import HttpResponse
# Create your views here.

def welcome(request):
	return render(request,"helloworld/welcome.html",{})
	#return HttpResponse("testing welcome")

def continent(request, continent_id):
	chosen_continent = Continent.objects.get(pk=continent_id)
	return render(request,"helloworld/continent.html",{"continent":chosen_continent})

	#return HttpResponse("continent %s" % continent_id)

def country_comment(request,continent_id, country_id):
	chosen_continent = Continent.objects.get(pk=continent_id)
	chosen_country = get_object_or_404(chosen_continent.country_set.all(), pk=country.id) 
	return render(request,"helloworld/country_comment.html",{"country":chosen_country})
	#return HttpResponse("country %s continent %s" % (country_id,continent_id))


def get_message(request,continent_id,country_id):
	chosen_country = Country.objects.get(pk=country_id)
	new_message = Message(author = request.POST["message_author"],
		message = request.POST["message_message"],country = chosen_country)
	return HttpResponseRedirect(reverse('country_comment', args=(continent_id,country_id)))



