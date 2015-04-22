import datetime
#import validators

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #Check for correctness


# You can find an example class diagram for the Model at
# http://yuml.me/edit/53759046
# You'll notice that the Model class provided by Django is
# elided (it doesn't have the attributes or methods listed.

class User(models.Model):
	
	user = models.OneToOneField(User)

	"""def __init__(self, username, first, last, password):
		self.first_name = first
		self.last_name = last
		self.password = password
		self.username = username
		self.is_staff = True
		self.is_active = True
	
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	password =models.CharField(max_length = 10)
	username = models.CharField(max_length = 10)
	is_staff = models.BooleanField(default= False)
	is_active = models.BooleanField(default = True)
	"""
	def Name(self):
		return self.user.first_name + " " + self.last_name
	
	def __unicode__(self):
		return self.user.username

class Cadet(User):
	
	
	def __init__(self, username, first, last, password, xnumber, company, sport):
		User.__init__(self, username, first, last, password)
		self.xNumber = xnumber
		self.company = company
		self.sport = sport
		self.is_staff = False
		
	xNumber = models.CharField(max_length = 6,default = 'x12345')
	company = models.CharField(max_length = 2)
	sport = models.CharField(max_length = 30)
	

#DateTimeField('date published')

class Meal(models.Model):
	
	BREAKFAST = 'BF'
	BRUNCH = 'BN'
	LUNCH = 'LU'
	DINNER = 'DN'
	meal_type_choices = (
		(BREAKFAST, 'Breakfast'),
		(BRUNCH, 'Brunch'),
		(LUNCH, 'Lunch'),
		(DINNER, 'Dinner'),
	)
	
	def __init__(self, date, meal_type, meal_description):
		self.date = date
		self.meal_type = meal_type
		self.meal_description = meal_description
	
	date = models.DateField('Meal Date')
	meal_type = models.CharField(max_length = 2, choices = meal_type_choices)
	meal_description = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.meal_date + " " + self.meal_type + " " + self.meal_description