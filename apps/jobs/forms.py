from django import forms
from .models import Job


class CreateJobsForm(forms.ModelForm):
	
	title = forms.CharField(widget = forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Titulo del puesto'
		}))
	description = forms.CharField(widget = forms.Textarea(attrs={
			'class': 'form-control',
			'placeholder': 'Descripcion del puesto',
			'rows': 4
		}))

	class Meta:
		model = Job
		fields = ('user', 'description', 'title', 'tag')
