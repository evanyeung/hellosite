from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from helloworld.redis_convinience import *
from helloworld import redisModels

from models import CommentList

class CommentListPlugin(CMSPluginBase):
	model = CommentList
	name = _("Comment List")
	render_template = "helloworld/comment_list_plugin.html"

	def render(self, context, instance, placeholder):
		context['instance'] = instance

		r = Redis(host='172.19.140.44', port=6379, db=0)
		country = instance.country.lower().title()
		cId = r.r.hget("countries:by:name", country)
		if cId:
			r.r.zinterstore("temp", ["messages:by:date", "country:" + str(cId) + ":messages"], aggregate="MAX")
			messages_id = r.r.zrange("temp", 0, 4, desc=True)
			messages = []
			for id in messages_id:
				message = r.get_json("message:" + str(id))
				messages.append(message)

			context['messages'] = messages

		return context

plugin_pool.register_plugin(CommentListPlugin)