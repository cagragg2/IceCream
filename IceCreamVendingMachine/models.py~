from django.db import models

# Create your models here.

class IceCream(models.Model):
	iceCreamID = models.IntegerField(default=0)
	iceCreamID.primary_key = True
	flavor = models.CharField(max_length=30)
	scoopable = models.CharField(max_length=1)
	description = models.CharField(max_length = 200)

	def __str__(self):
		return self.flavor


class Stores(models.Model):
	storeID = models.IntegerField(default=0)
	storeID.primary_key = True
	storeName = models.CharField(max_length=30)
	city = models.CharField(max_length = 30)
	state = models.CharField(max_length = 2)

	def __str__(self):
		return self.storeName

class SnowCone(models.Model):
	snowConeID = models.IntegerField(default=0)
	snowConeID.primary_key = True
	coneFlavor = models.CharField(max_length=30)
	coneDescription = models.CharField(max_length=200)

	def __str__(self):
		return self.coneFlavor

class WhereOff(models.Model):
	ID = models.IntegerField(default=0)
	ID.primary_key = True
	stores = models.ForeignKey(Stores)
	icecream = models.ForeignKey(IceCream)
	snowcone = models.ForeignKey(SnowCone)
	
	def __str__(self):
		return self.ID

class WhereOffAmounts(models.Model):
	ID = models.IntegerField(default=0)
	ID.primary_key = True
	stores = models.ForeignKey(Stores)
	icecream = models.ForeignKey(IceCream)
	quantity = models.IntegerField(default=0)
	price = models.FloatField(default=0)

