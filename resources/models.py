
from django.db import models

class Course(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	duration = models.PositiveIntegerField(help_text="Duration in hours")

	def __str__(self):
		return self.title

class Trainer(models.Model):
	name = models.CharField(max_length=100)
	bio = models.TextField()
	experience_years = models.PositiveIntegerField()

	def __str__(self):
		return self.name

class Announcement(models.Model):
	title = models.CharField(max_length=200)
	message = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
