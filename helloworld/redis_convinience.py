class redis(object):
	def __init__(self, host, port, db):
		r = redis.StrictRedis(host=host, port=port, db=db)

	def initdb():
		r.flushdb()
		r.set("continent:next:id", 0)
		r.set("country:next:id", 0)
		r.set("message:next:id", 0)

	def get_next_id(self, model):
		'''
		model should be continent, country, or message
		returns the next id of that model
		'''
		id = r.incr( model + ":next:id")

		return id

	def add_continent(self, cont):
		p = r.pipeline()
		p.set("continent:" + cont.id, cont)
		p.hset("continents:by:name", cont.name, cont.id)
		return p.execute()

	def add_country(self, country):
		p = r.pipeline()
		p.set("country:" + country.id, country)
		p.hset("countries:by:name", country.name, country.id)
		p.sadd("continent:" + country.cont_id + "countries", country.id)
		return p.execute()

	def add_message(self, message):
		p = r.pipeline()
		p.set("message:" + message.id, message)
		p.zadd("messages:by:date", message.date, message.id)
		p.sadd("country:" + message.country_id + "messages", message.id)
		return p.execute()