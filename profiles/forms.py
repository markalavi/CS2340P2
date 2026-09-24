from typing import ClassVar

from django import forms

from profiles.models import Education, Experience, Link, Skill


class AddLinkForm(forms.ModelForm):
	class Meta:
		model = Link
		fields: ClassVar[list[str]] = ['label', 'url']


class AddEducationForm(forms.ModelForm):
	class Meta:
		model = Education
		fields: ClassVar[list[str]] = ['school', 'degree', 'start_year', 'end_year']


class AddWorkForm(forms.ModelForm):
	class Meta:
		model = Experience
		fields: ClassVar[list[str]] = ['company', 'title', 'description', 'start_date', 'end_date']


class AddSkillForm(forms.Form):
	skill = forms.CharField(
		max_length=50,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'list': 'skill-options',
				'autocomplete': 'off',
				'placeholder': 'Type or pick a skill',
			}
		),
	)

	def __init__(self, *args, profile=None, **kwargs):
		super().__init__(*args, **kwargs)
		qs = Skill.objects.order_by('name')
		if profile is not None:
			qs = qs.exclude(profile=profile) 
		self.suggestions = qs
