from django.contrib import admin

from profiles.models import Education, Link, Profile, Skill

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Link)
admin.site.register(Education)
