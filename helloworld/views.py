from django.shortcuts import render,get_object_or_404
from django.http import Http404
from helloworld.models import Continent ,Country, Message
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.generic.base import View

from django.template.loader import get_template
from django.template import Context

import simplejson as json
from django.core import serializers

from helloworld.redis_convinience import *

def connect_to_redis():
	r = Redis(host='172.19.140.24', port=6379, db=0)
	return r

#need continents on every page for navbar
def get_continents():
	r = connect_to_redis()
	continents = r.get_all("continent")

	for cont in continents:
		country_set = []
		ids = r.r.smembers("continent:" + str(cont['id']) + ":countries")
		for id in ids:
			country = r.get_json("country:" + id)
			country_set.append(country)
		cont['country_set'] = country_set

	return continents

def welcome(request):
	r = connect_to_redis()
	continents = get_continents()
	canada = r.r.hget("countries:by:name", "Canada")
	return render(request,"helloworld/welcome.html",{"continents": continents, "canada": canada})


def continent(request, continent_id):
	r = connect_to_redis()
	continents = get_continents()
	chosen_continent = r.get_json("continent:" + str(continent_id))
	if not chosen_continent:
		raise Http404

	country_set = []
	ids = r.r.smembers("continent:" + str(chosen_continent['id']) + ":countries")
	for id in ids:
		country = r.get_json("country:" + id)
		country_set.append(country)
	chosen_continent['country_set'] = country_set

	return render(request,"helloworld/continent.html",{"continent":chosen_continent, "continents": continents})


def country_comment(request, country_id):
	r = connect_to_redis()
	continents = get_continents()
	chosen_country = get_object_or_404(Country, pk=country_id)
	messages = chosen_country.message_set.order_by('-pub_date')[:5]
	return render(request,"helloworld/country_comment.html",{"country":chosen_country, "continents": continents, "messages": messages})


def get_message(request,country_id):
	r = connect_to_redis()
	continents = get_continents()
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
'''
def ajax(request):
	if request.is_ajax():
		print "ajax"
		return HttpResponse("It Worked!!")
	else:
		print "getted"
		return HttpResponse("get")
'''

class ajax(View):

	r = connect_to_redis()

	def post(self, request):

		chosen_country = get_object_or_404(Country, pk=request.POST['country_id'])

		new_message = Message(author = request.POST["message_author"],
						  message = request.POST["message_message"],
						  country = chosen_country,
						  pub_date = timezone.now()
						  )
		new_message.save()

		data = {}
		t = get_template('helloworld/comment_list.html')
		c = Context({'messages': chosen_country.message_set.order_by('-pub_date')[:5]})
		data = t.render(c)
		#data["html"] = str(render(request, 'helloworld/comment_list.html', chosen_country.message_set.order_by('-pub_date')[:5]))
		#data = json.dumps( {"hello": "<p>Hello</p>"} )
		return HttpResponse( json.dumps(data), content_type='application/json')


def form_test(request):
	return render(request,"helloworld/form_test.html")