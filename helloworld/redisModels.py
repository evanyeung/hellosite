class Continent(object):

	def __init__(self, name, area):
		id = get_next_id("continent")
		name = name
		area = area


class Country(object):

	def __init__ (self, name, population, continent):
		id = get_next_id("country")
		name = name
		population = population
		cont_id = cont_id

class Message(object):

	def __init__ (self, author, message, country):
		id = get_next_id("message")
		pub_date = get_pub_date() #held in unix time
		author = author
		message = message
		country_id = country_id