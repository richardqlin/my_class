from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


STATE_CHOICES={
	('CA','California'),
	('NY','New York'),
	('TX','Texas'),
	('WA','Washington')
}
class Question(models.Model):
	question_text =models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')

	def __unicode__(self):
		return self.question_text

	def was_published_recently(self):
		now =timezone.now()
		return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
	question =models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_text

class UserProfile(models.Model):
	firstname=models.CharField(max_length=30)
	lastname=models.CharField(max_length=30)
	age=models.IntegerField()
	email=models.EmailField()
	street=models.CharField(max_length=50)
	city=models.CharField(max_length=50)
	state=models.CharField(max_length=30, choices=STATE_CHOICES)

	def __unicode__(self):
		return "%s - %s" %(self.firstname, self.lastname)

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()
	
	def __unicode__(self):
		return self.name
		
		
class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()
	def __unicode__(self):
		return self.title
