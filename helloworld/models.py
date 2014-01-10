from django.db import models

# Create your models here.
class Continent(models.Model):
	name = models.CharField(max_length=15)
	area = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

class Country(models.Model):
	continent = models.ForeignKey(Continent)
	name = models.CharField(max_length=50)
	population = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

class Message(models.Model):
	country = models.OneToOneField(Country)
	author = models.CharField(max_length=50)
	message = models.CharField(max_length=500)

	def __unicode__(self):
		return self.country + self.author