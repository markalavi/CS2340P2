from django.http import HttpResponse

def job_recommendations(request, job_id):
    return HttpResponse(f'Recommendations for job {job_id}')