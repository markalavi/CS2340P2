from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from accounts.models import User

# The roles that should be allowed to access any views decorated
# with `recruiter_required`.
recruiter_only_roles = [User.UserType.Recruiter, User.UserType.Admin]
# The roles that should be allowed to access any views decorated
# with `jobseeker_required`.
jobseeker_only_roles = [User.UserType.Recruiter, User.UserType.Admin]

def recruiter_required(view_func):
	"""
	Restricts a view to authenticated users with the roles in
	`accounts.decorators.recruiter_only_roles`
	"""

	@login_required
	@wraps(view_func)
	def wrapper(request, *args, **kwargs):
		if request.user.user_type not in recruiter_only_roles:
			raise PermissionDenied
		return view_func(request, *args, **kwargs)

	return wrapper


def jobseeker_required(view_func):
	"""
	Restricts a view to authenticated users with the roles in
	`accounts.decorators.jobseeker_only_roles`
	"""

	@login_required
	@wraps(view_func)
	def wrapper(request, *args, **kwargs):
		if request.user.user_type not in jobseeker_only_roles:
			raise PermissionDenied
		return view_func(request, *args, **kwargs)

	return wrapper

