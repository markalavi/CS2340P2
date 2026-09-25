from django.urls import path

from jobs import views

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='list'),
    path('new/', views.job_create, name='create'),
    path('browse/', views.job_browse, name='browse'),
    path('<int:pk>/', views.job_detail, name='detail'),
    path('<int:pk>/edit/', views.job_edit, name='edit'),
]
