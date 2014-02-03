
def continent(name, area, r):
	cont = {}
	cont['id'] = r.get_next_id("continent")
	cont['name'] = name
	cont['area'] = area
	return cont


def country(name, population, cont_id, r):
	country = {}
	country['id'] = r.get_next_id("country")
	country['name'] = name
	country['population'] = population
	country['cont_id'] = cont_id
	return country


def message(author, message, country, r):
	message = {}
	message['id'] = r.get_next_id("message")
	message['pub_date'] = get_pub_date() #held in unix time
	message['author'] = author
	message['message'] = message
	message['country_id'] = country_id
	return message