from django.db import models

# Create your models here.
class Continent(models.Model):
	name = models.CharField(max_length=10)
	area = models.IntegerField(default=0)

class Country(models.Model):
	continent = models.ForeignKey(Continent)
	name = models.CharField(max_length=50)
	population = models.IntegerField(default=0)

class Message(models.Model):
	country = models.OneToOneField(Country)
	author = models.CharField(max_length=50)
	message = models.CharField(max_length=500)