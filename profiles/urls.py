from django.contrib import admin
from django.urls import include, path

from profiles.views import profile_me

urlpatterns = [
    path('', profile_me)
]
