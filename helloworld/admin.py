from django.contrib import admin
from helloworld.models import Continent, Country, Message
# Register your models here.
admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Message)