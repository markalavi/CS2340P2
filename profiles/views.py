from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from profiles.forms import AddEducationForm, AddLinkForm, AddSkillForm, AddWorkForm
from profiles.models import Profile, Skill


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


@login_required
def profile_me_add_work(request):
	profile, _ = Profile.objects.get_or_create(user=request.user)

	if request.method == 'POST':
		form = AddWorkForm(request.POST)

		if form.is_valid():
			link = form.save(commit=False)
			link.profile = profile
			link.save()

			return redirect('/profiles')
	else:
		form = AddWorkForm()

	data = {'template_data': {'title': 'Add Link', 'form': form}}
	return render(request, 'profiles/add_work.html', data)


@login_required
def profile_me_add_skill(request):
	profile, _ = Profile.objects.get_or_create(user=request.user)

	if request.method == 'POST':
		form = AddSkillForm(request.POST, profile=profile)
		if form.is_valid():
			name = form.cleaned_data['skill']
			skill, _ = Skill.objects.get_or_create(
				name__iexact=name,
				defaults={'name': name},
			)
			profile.skills.add(skill)
			return redirect('/profiles')
	else:
		form = AddSkillForm(profile=profile)

	data = {'template_data': {'title': 'Add Skill', 'form': form}}
	return render(request, 'profiles/add_skill.html', data)
