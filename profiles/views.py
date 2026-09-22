from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from profiles.models import Profile


@login_required
def profile_me(request):
	profile, created = Profile.objects.get_or_create(user=request.user)

	if not created:
		redirect('/')

	data = {'template_data': {'title': 'My Profile', 'profile': profile}}

	return render(request, 'profiles/profile_me.html', data)
