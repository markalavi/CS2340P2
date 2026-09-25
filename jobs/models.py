from django.db import models

from accounts.models import User
from profiles.models import Skill


class Job(models.Model):
    """Represents a job listing posted by a recruiter on the site."""

    id = models.AutoField(primary_key=True)

    # The recruiter that posted the job listing
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)

    # The job title
    title = models.CharField(max_length=150)

    # Where the job is located
    location = models.CharField(max_length=100, blank=True)

    # The job description
    description = models.TextField(max_length=1024)

    # Annualized salary standardized in cents.
    annual_salary_in_cents = models.IntegerField()

    # Skills needed by the job.
    skills = models.ManyToManyField(Skill)

    # TODO: Create a Company model and make a foreign key to enable search by company.
    company = models.CharField(max_length=40)

    # When the job was posted.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the job name and the company name"""
        return f'{self.title}, {self.company}'
