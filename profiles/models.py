from django.conf import settings
from django.db import models


class Skill(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		"""Return the name of the skill as a string for admin panel."""
		return f'{self.name}'


class Profile(models.Model):
	# NOTE: Automatically delete entry when corresponding User model is deleted
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	headline = models.CharField(max_length=120, blank=True)
	location = models.CharField(max_length=100, blank=True)
	skills = models.ManyToManyField(Skill, blank=True)


class Education(models.Model):
	profile = models.ForeignKey(Profile, related_name='education', on_delete=models.CASCADE)
	school = models.CharField(max_length=100, blank=True)
	degree = models.CharField(max_length=100, blank=True)

	start_year = models.PositiveIntegerField()
	end_year = models.PositiveIntegerField(null=True, blank=True)  # null if currently enrolled


class Experience(models.Model):
	profile = models.ForeignKey(Profile, related_name='experience', on_delete=models.CASCADE)
	company = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	start_date = models.DateField()
	end_date = models.DateField(null=True, blank=True)


class Link(models.Model):
	profile = models.ForeignKey(Profile, related_name='links', on_delete=models.CASCADE)
	label = models.CharField(max_length=50)
	url = models.URLField()
