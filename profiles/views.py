from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile_me(request):
	data = {'template_data': {'title': 'My Profile'}}

	return render(request, 'profiles/profile_me.html', data)
