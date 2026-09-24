from typing import ClassVar

from django import forms

from profiles.models import Education, Link


class AddLinkForm(forms.ModelForm):
	class Meta:
		model = Link
		fields: ClassVar[list[str]] = ['label', 'url']


class AddEducationForm(forms.ModelForm):
	class Meta:
		model = Education
		fields: ClassVar[list[str]] = ['school', 'degree', 'start_year', 'end_year']
