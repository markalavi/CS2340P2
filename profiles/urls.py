from django.urls import path

from profiles.views import (
    profile_me,
    profile_me_add_education,
    profile_me_add_link,
    profile_me_add_skill,
    profile_me_add_work,
    profile_me_edit_info,
)

app_name = 'profiles'

urlpatterns = [
    path('', profile_me, name='me'),
    path('me/add_link/', profile_me_add_link, name='add_link'),
    path('me/add_education/', profile_me_add_education, name='add_education'),
    path('me/add_work/', profile_me_add_work, name='add_work'),
    path('me/add-skill/', profile_me_add_skill, name='add_skill'),
    path('me/edit/', profile_me_edit_info, name='edit_info'),
]
