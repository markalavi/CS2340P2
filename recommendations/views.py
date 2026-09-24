from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

from accounts.models import User
from jobs.models import Job
from profiles.models import Profile
from recommendations.scoring import candidate_score

@login_required
def job_recommendations(request):
    # this page is only for job seekers
    if request.user.user_type != User.UserType.JobSeeker:
        raise PermissionDenied

    # ensure the job seeker has a profile
    profile, _ = Profile.objects.get_or_create(user=request.user)

    # convert the job seeker's skills to a set of db IDs
    candidate_skill_ids = set(profile.skills.values_list('id', flat=True))

    # prefetch required skills 
    jobs = Job.objects.select_related('recruiter').prefetch_related('required_skills')
    recommendations = []

    for job in jobs:
        required_skills = list(job.required_skills.all())
        required_skill_ids = {skill.id for skill in required_skills}

        score = candidate_score(required_skill_ids, candidate_skill_ids)

        # only recommend jobs that have at least 1 matching skill.
        if score > 0:
            matching_skills = [skill for skill in required_skills if skill.id in candidate_skill_ids]
            recommendations.append(
                {
                    'job': job,
                    'score': score,
                    'match_percentage': round(score * 100),
                    'matching_skills': matching_skills,
                }
            )
        # Highest match first, with job ID providing consistent ordering for ties
    recommendations.sort(key=lambda recommendation: (-recommendation['score'], recommendation['job'].id,))

    context = {
        'template_data': {
            'title': 'Recommended Jobs',
            'recommendations': recommendations,
        }
    }

    return render(request, 'recommendations/job_recommendations.html', context)
