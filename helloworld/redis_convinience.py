import redis
import simplejson as json

'''
convinent methods when connecting to redis with helloworld app
Use a r = Redis(args)
r.r.[command] to execute other commands
'''

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
		p.sadd("continent:" + str(country['cont_id']) + ":countries", country['id'])
		return p.execute()

	def add_message(self, message):
		jmessage = json.dumps("message")
		p = self.r.pipeline()
		p.set("message:" + str(message['id']), jmessage)
		p.zadd("messages:by:date", message['date'], message['id'])
		p.sadd("country:" + str(message['country_id)']) + "messages", message['id'])
		return p.execute()

	def get_json(self, key):
		i = self.r.get(key)
		if i:
			i = json.loads(i)
			return i

	#get and set to be used on key value pairs not related to obj
	def get(self, key):
		i = self.get(key)
		return i

	def set(self, key, value):
		i = self.set(key, value)
		return i

	def get_all(self, model):
		max_id = int(self.r.get(model + ":next:id"))+1
		lst = []
		for i in range(1, max_id):
			j = self.get_json(model + ":" + str(i))
			if j:
				lst.append(j)
		return lst