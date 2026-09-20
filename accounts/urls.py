from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import include, path

from accounts import views
from accounts.forms import LoginForm

app_name = 'accounts'

urlpatterns = [
	path(
		'login/',
		LoginView.as_view(template_name='accounts/login.html', authentication_form=LoginForm),
		name='login',
	),

	path('signup/', views.signup, name='signup'),
]
