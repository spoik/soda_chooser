from django.db import models

# Create your models here.

class Beverage(models.Model):
	name = models.CharField(max_length=50)
	would_drink = models.IntegerField(default=0)
	would_not_drink = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name
