from django.contrib import admin
from django.urls import include, path

from profiles.views import profile_me

app_name = 'profiles'

urlpatterns = [path('', profile_me, name='me')]
