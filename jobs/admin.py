from django.contrib import admin

from .models import Job


class CustomJobAdmin(admin.ModelAdmin):
    """Admin registration for jobs."""

    list_display = [
        'id',
        'recruiter',
        'title',
        'location',
        'description',
        'annual_salary_in_cents',
        'company',
        'created_at',
    ]

admin.site.register(Job, CustomJobAdmin)
