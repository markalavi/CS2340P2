from django.urls import path

from . import views

app_name = 'recommendations' # prefix for all URL labels (avoids collisions)

urlpatterns = [
  path('jobs/<int:job_id>/', views.job_recommendations, name='for_job') 
]