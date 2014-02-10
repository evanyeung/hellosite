from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.views.generic.base import View

from django.utils import timezone
from datetime import datetime
import pytz

from django.template.loader import get_template
from django.template import Context

import simplejson as json

from helloworld.redis_convinience import *
from helloworld import redisModels

def connect_to_redis():
	r = Redis(host='172.19.140.44', port=6379, db=0)
	return r

#need continents on every page for navbar
def get_continents():
	r = connect_to_redis()
	continents = r.get_all("continent")

	for cont in continents:
		country_set = []
		ids = r.r.smembers("continent:" + str(cont['id']) + ":countries")
		for id in ids:
			country = r.get_json("country:" + str(id))
			country_set.append(country)
		cont['country_set'] = country_set

	return continents

def welcome(request):
	r = connect_to_redis()
	continents = get_continents()
	canada_id = r.r.hget("countries:by:name", "Canada")
	canada = r.get_json("country:" + str(canada_id))
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
		country = r.get_json("country:" + str(id))
		country_set.append(country)
	chosen_continent['country_set'] = country_set

	return render(request,"helloworld/continent.html",{"continent":chosen_continent, "continents": continents})


def country_comment(request, country_id):
	r = connect_to_redis()
	continents = get_continents()
	chosen_country = r.get_json("country:" + str(country_id))
	if not chosen_country:
		raise Http404

	r.r.zinterstore("temp", ["messages:by:date", "country:" + str(chosen_country['id']) + ":messages"], aggregate="MAX")
	messages_id = r.r.zrange("temp", 0, 4, desc=True)
	messages = []
	for id in messages_id:
		message = r.get_json("message:" + str(id))
		messages.append(message)

	return render(request,"helloworld/country_comment.html",{"country":chosen_country, "continents": continents, "messages": messages})

class ajax(View):

	def post(self, request):

		r = connect_to_redis()

		chosen_country = r.get_json("country:" + str(request.POST['country_id']))
		if not chosen_country:
			raise Http404

		local_tz = pytz.timezone('America/Toronto')

		unix_time = local_tz.localize(datetime(1970, 1, 1))

		new_message = redisModels.message(author = request.POST["message_author"],
						 					comment = request.POST["message_comment"],
											country_id = chosen_country['id'],
											pub_date = (timezone.now() - unix_time).total_seconds(),
											r = r
											)
		r.add_message(new_message)

		t = get_template('helloworld/comment_list.html')
		r.r.zinterstore("temp", ["messages:by:date", "country:" + str(chosen_country['id']) + ":messages"], aggregate="MAX")
		messages_id = r.r.zrange("temp", 0, 4, desc=True)
		messages = []
		for id in messages_id:
			message = r.get_json("message:" + str(id))
			messages.append(message)

		c = Context({'messages': messages})
		data = t.render(c)

		return HttpResponse( json.dumps(data), content_type='application/json')
