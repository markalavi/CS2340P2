from typing import ClassVar

from django import forms

from profiles.models import Education, Experience, Link


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
