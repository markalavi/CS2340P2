from django.urls import path
from recommendations import views

app_name = 'recommendations'

urlpatterns = [
    path('', views.job_recommendations, name='jobs')
]
