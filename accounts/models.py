from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	"""
	Represents a user of the website. Recruiter or applicant is set
	by the `account_type` field.
	"""

	class UserType(models.TextChoices):
		"""Represents user types"""

		#        DB name, Human-readable name
		JobSeeker = ('JS', 'Job Seeker')
		Recruiter = ('R', 'Recruiter')
		Admin = ('A', 'Administrator')

	class Meta:
		"""Provides constraints for the parent class fields."""

		constraints: ClassVar[list[models.UniqueConstraint]] = [
			models.UniqueConstraint(fields=['email'], name='unique_user_email'),
		]

	# Unique user ID.
	id = models.AutoField(primary_key=True)
	# Distinguishes which UI to show user.
	user_type = models.CharField(max_length=2, choices=UserType.choices, default=UserType.JobSeeker)
	# User details
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)

	REQUIRED_FIELDS: ClassVar[list[str]] = ['first_name', 'last_name', 'user_type']

	def __str__(self):
		"""Returns display name for admin panel, in form \"1: lah8@abc.com\""""
		return f'{self.id}: {self.email}'
