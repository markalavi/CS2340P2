from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from profiles.forms import AddEducationForm, AddLinkForm
from profiles.models import Profile


@login_required
def profile_me(request):
	profile, _ = Profile.objects.get_or_create(user=request.user)

	data = {'template_data': {'title': 'My Profile', 'profile': profile}}

	return render(request, 'profiles/profile_me.html', data)


@login_required
def profile_me_add_education(request):
	profile, _ = Profile.objects.get_or_create(user=request.user)

	if request.method == 'POST':
		form = AddEducationForm(request.POST)

		if form.is_valid():
			education = form.save(commit=False)
			education.profile = profile
			education.save()

			return redirect('/profiles')
	else:
		form = AddEducationForm()

	data = {'template_data': {'title': 'Add Link', 'form': form}}
	return render(request, 'profiles/add_education.html', data)


@login_required
def profile_me_add_link(request):
	profile, _ = Profile.objects.get_or_create(user=request.user)

	if request.method == 'POST':
		form = AddLinkForm(request.POST)

		if form.is_valid():
			link = form.save(commit=False)
			link.profile = profile
			link.save()

			return redirect('/profiles')
	else:
		form = AddLinkForm()

	data = {'template_data': {'title': 'Add Link', 'form': form}}
	return render(request, 'profiles/add_link.html', data)
