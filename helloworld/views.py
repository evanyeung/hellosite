from django.shortcuts import render,get_object_or_404
from helloworld.models import Continent ,Country, Message
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.generic.base import View

import simplejson as json
from django.core import serializers
# Create your views here.

def welcome(request):
	continents = Continent.objects.all()
	canada = Country.objects.get(name="Canada")
	return render(request,"helloworld/welcome.html",{"continents": continents, "canada": canada})


def continent(request, continent_id):
	continents = Continent.objects.all()
	chosen_continent = get_object_or_404(Continent, pk=continent_id)
	return render(request,"helloworld/continent.html",{"continent":chosen_continent, "continents": continents})


def country_comment(request, country_id):
	continents = Continent.objects.all()
	chosen_country = get_object_or_404(Country, pk=country_id)
	messages = chosen_country.message_set.order_by('-pub_date')[:5]
	return render(request,"helloworld/country_comment.html",{"country":chosen_country, "continents": continents, "messages": messages})


def get_message(request,country_id):
	continents = Continent.objects.all()
	chosen_country = get_object_or_404(Country, pk=country_id)
	messages = chosen_country.message_set.order_by('-pub_date')[:5]

	if (not request.POST["message_author"]):
		return render(request, "helloworld/country_comment.html", {"country":chosen_country, "continents": continents, "messages": messages, "error": "You did not enter an author!"})
	elif(not request.POST["message_message"]):
		return render(request, "helloworld/country_comment.html", {"country":chosen_country, "continents": continents, "messages": messages, "error": "You did not enter a message!"})
		
	new_message = Message(author = request.POST["message_author"],
						  message = request.POST["message_message"],
						  country = chosen_country,
						  pub_date = timezone.now()
						  )
	new_message.save()
	return HttpResponseRedirect(reverse('country_comment', args=(country_id,)))

def ajax(request):
	if request.is_ajax():
		print "ajax"
		return HttpResponse("It Worked!!")
	else:
		print "getted"
		return HttpResponse("get")

'''
class ajax(View):
	def get(self, request):
		print "getted"
		return HttpResponse("get")

	def post(self, request):
		print "posted"
		return HttpResponse("posted")
		chosen_country = get_object_or_404(Country, pk=request.POST['country_id'])

		new_message = Message(author = request.POST["message_author"],
						  message = request.POST["message_message"],
						  country = chosen_country,
						  pub_date = timezone.now()
						  )
		new_message.save()

		data = serializers.serialize('json', chosen_country.message_set.order_by('-pub_date')[:5])


		return HttpResponse(data, content_type='application/json')
'''

def form_test(request):
	return render(request,"helloworld/form_test.html")