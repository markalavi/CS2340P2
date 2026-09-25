from django.db import models

from accounts.models import User
from jobs.models import Job


class Application(models.Model):
    """Represents a job application made by a job seeker to a Job."""

    class ApplicationStatus(models.IntegerChoices):
        """Represents the application status for recruiter Kanban Board."""

        InConsideration = 1, 'In Consideration'
        Rejected = 2, 'Rejected'
        FirstRound = 3, 'First Round'
        SecondRound = 4, 'Second Round'
        OfferExtended = 5, 'Offer Extended'

    id = models.AutoField(primary_key=True)

    # The user that is applying for this job.
    applicant_user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The job the user applied for
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    # Allows sorting by date on both user side and recruiter side.
    date = models.DateTimeField(auto_now_add=True)

    # Current applicant status, enables recruiter Kanban Board view.
    status = models.IntegerField(
        choices=ApplicationStatus.choices, default=ApplicationStatus.InConsideration
    )
