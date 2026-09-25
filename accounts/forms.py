from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'user_type',
            'password1',
            'password2',
        )

    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(
        choices=[(User.UserType.JobSeeker, 'Job Seeker'), (User.UserType.Recruiter, 'Recruiter')]
    )
