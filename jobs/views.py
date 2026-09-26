from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.decorators import recruiter_required
from accounts.models import User
from applications.models import Application
from jobs.forms import JobForm
from jobs.models import Job


@recruiter_required
def job_list(request):
    jobs = Job.objects.filter(recruiter=request.user).order_by('-created_at')
    data = {'template_data': {'title': 'My Job Postings', 'jobs': jobs}}
    return render(request, 'jobs/job_list.html', data)


@recruiter_required
def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()
            form.save_m2m()
            return redirect('jobs:list')
    else:
        form = JobForm()

    data = {'template_data': {'title': 'Post a Job', 'form': form}}
    return render(request, 'jobs/job_form.html', data)


@recruiter_required
def job_edit(request, pk):
    job = get_object_or_404(Job, pk=pk, recruiter=request.user)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('jobs:list')
    else:
        form = JobForm(instance=job)

    data = {'template_data': {'title': 'Edit Job', 'form': form, 'job': job}}
    return render(request, 'jobs/job_form.html', data)


@login_required
def job_browse(request):
    jobs = Job.objects.all().order_by('-created_at')
    data = {'template_data': {'title': 'Browse Jobs', 'jobs': jobs}}
    return render(request, 'jobs/job_browse.html', data)


@login_required
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)

    already_applied = False
    if request.user.user_type == User.UserType.JobSeeker:
        already_applied = Application.objects.filter(applicant_user=request.user, job=job).exists()

    data = {
        'template_data': {
            'title': job.title,
            'job': job,
            'already_applied': already_applied,
        }
    }
    return render(request, 'jobs/job_detail.html', data)
