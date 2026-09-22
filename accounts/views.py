from django.contrib.auth import login
from django.shortcuts import redirect, render

from accounts.forms import SignupForm


def signup(request):
	if request.user.is_authenticated:
		return redirect('/')

	form = SignupForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		user = form.save()
		login(request, user)
		return redirect('/')

	return render(
		request, 'accounts/signup.html', {'template_data': {'title': 'Sign Up', 'form': form}}
	)
