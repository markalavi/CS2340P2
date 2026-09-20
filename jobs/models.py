from django.db import models
from accounts.models import User


class Job(models.Model):
	"""Represents a job listing posted by a recruiter on the site."""

	id = models.AutoField(primary_key=True)

	# The recruiter that posted the job listing
	recruiter = models.ForeignKey(User, on_delete=models.CASCADE)

	# The job description
	description = models.TextField(max_length=1024)

	# Annualized salary standardized in cents.
	annual_salary_in_cents = models.IntegerField()
