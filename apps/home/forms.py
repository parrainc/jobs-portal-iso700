from django import forms
from django.contrib.auth.models import User 

from apps.jobs.models import Job, Tag

class LoginForm(forms.ModelForm):

	username = forms.CharField(widget = forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Username'
		}))
	password = forms.CharField(widget = forms.PasswordInput(attrs={
			'class': 'form-control',
			'placeholder': 'Password'
		}))

	class Meta:
		model = User
		fields = ('username', 'password')


class CreateJobsForm(forms.ModelForm):
	
	title = forms.CharField(widget = forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Titulo del empleo'
		}))
	description = forms.CharField(widget = forms.Textarea(attrs={
			'class': 'form-control',
			'placeholder': 'Descripción del puesto',
			'rows': 4
		}))
	email = forms.EmailField(widget = forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'tu@correo.com'
		}))
	tags = forms.CharField(widget = forms.TextInput(attrs={
			'class': 'form-control',
		}))
	published_by = forms.CharField(widget = forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Publicado por: [Opcional]'
		}))


	class Meta:
		model = Job
		fields = ('user', 'description', 'title', 'tag')

			
