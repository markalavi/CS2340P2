from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
	"""Admin registration for user models."""

	model = User

	list_display = ['id', 'email', 'username', 'first_name', 'last_name']


admin.site.register(User, CustomUserAdmin)
