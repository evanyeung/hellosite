import redis
import simplejson as json

class Redis(object):

	def __init__(self, host, port, db):
		self.r = redis.StrictRedis(host=host, port=port, db=db)

	def initdb(self):
		self.r.flushdb()
		self.r.set("continent:next:id", 0)
		self.r.set("country:next:id", 0)
		self.r.set("message:next:id", 0)

	def get_next_id(self, model):
		'''
		model should be continent, country, or message
		returns the next id of that model
		'''
		id = self.r.incr( model + ":next:id")

		return id

	def add_continent(self, cont):
		jcont = json.dumps(cont)
		p = self.r.pipeline()
		p.set("continent:" + str(cont['id']), jcont)
		p.hset("continents:by:name", cont['name'], cont['id'])
		return p.execute()

	def add_country(self, country):
		jcountry = json.dumps(country)
		p = self.r.pipeline()
		p.set("country:" + str(country['id']), jcountry)
		p.hset("countries:by:name", country['name'], country['id'])
		p.sadd("continent:" + str(country['cont_id']) + "countries", country['id'])
		return p.execute()

	def add_message(self, message):
		jmessage = json.dumps("message")
		p = self.r.pipeline()
		p.set("message:" + str(message['id']), jmessage)
		p.zadd("messages:by:date", message['date'], message['id'])
		p.sadd("country:" + str(message['country_id)']) + "messages", message['id'])
		return p.execute()

	def get(self, key):
		i = self.r.get(key)
		i = json.loads(i)
		return i