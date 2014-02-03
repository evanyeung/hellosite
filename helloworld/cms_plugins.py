from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from helloworld.models import plugincountry
from django.utils.translation import ugettext as _

class countryPlugin(CMSPluginBase):
    model = plugincountry # Model where data about this plugin is saved
    name = _("country plugin") # Name of the plugin
    render_template = "helloworld/plugin.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'country':instance.country,'messages':instance.country.messages.all})
        return context

plugin_pool.register_plugin(countryPlugin) # register the plugin