from typing import ClassVar

from django import forms

from jobs.models import Job


class JobForm(forms.ModelForm):
    annual_salary = forms.DecimalField(
        label='Annual salary (USD)',
        max_digits=10,
        decimal_places=2,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Job
        fields: ClassVar[list[str]] = ['title', 'company', 'location', 'description', 'skills']
        widgets: ClassVar[dict[str, any]] = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'skills': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['annual_salary'].initial = self.instance.annual_salary_in_cents / 100

    def save(self, commit=True):
        job = super().save(commit=False)
        job.annual_salary_in_cents = int(self.cleaned_data['annual_salary'] * 100)
        if commit:
            job.save()
            self.save_m2m()
        return job
