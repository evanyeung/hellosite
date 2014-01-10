from django.db import models

class countries(model.Model):
# Create your models here.
class Continent(models.Models):
	name = models.CharField(max_length=10)
	area = models.IntegerField(Default=0)

class Country(models.Models):
	continent = models.ForeignKey(Continent)
	name = models.CharField(max_length=50)
	population = models.IntegerField(Default=0)

class Message(models.Models):
	country = models.OneToOneField(Country)
	author = models.CharField(max_length=50)
	message = models.CharField(max_length=500)
