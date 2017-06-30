from django.db import models

# Create your models here.
CITY_CHOICES = (
	(u'Vadodara',u'Vadodara'),
	(u'Ahmedabad',u'Ahmedabad'),
	(u'Amravati',u'Amravati'),
	(u'Aurangabad',u'Aurangabad'),
	(u'Bangalore',u'Bangalore'),
	(u'Bhopal',u'Bhopal'),
	(u'Indore',u'Indore'),
	(u'Jodhpur',u'Jodhpur'),
	(u'Pune',u'Pune'),
	(u'Raipur',u'Raipur'),
	(u'Trivandrum',u'Trivandrum'),
	(u'Kota',u'Kota'),
	(u'Lucknow',u'Lucknow'),
	)
LEVEL_CHOICES = (
	(u'8-10',u'8th to 10th Standard'),
	(u'11-12',u'11th or 12th Standard'),
	)


class Register(models.Model):
	city = models.CharField(max_length = 120, choices = CITY_CHOICES)
	level = models.CharField(max_length = 120, choices = LEVEL_CHOICES)
	name = models.CharField(max_length = 120)
	email = models.EmailField()
	phone = models.CharField(max_length = 10)

	def __str__(self):
		return (self.city + ' | ' + self.level + ' | ' + self.name)