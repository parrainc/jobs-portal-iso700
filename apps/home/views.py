import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, View
from django.core import serializers
from django.http import HttpResponse, Http404, HttpResponseRedirect

from apps.jobs.models import Job, Tag
from .forms import LoginForm

class IndexView(ListView):
	template_name = 'home/index.html'

	def get_queryset(self):
		queryset = Job.objects.all().order_by('-created')[:10]
		tags = [ job.tag.all() for job in queryset]
		return zip(queryset, tags)


class LoginView(View):
	
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return render(request, 'home/login_form.html')
		else:
			return redirect('/')

	def post(self, request, *args, **kwargs):
		logout(request)

		if request.POST:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(
				username = username, 
				password = password
			)
			if user is not None:
				login(request, user)
				try:
					return HttpResponseRedirect(request.GET['next'])
				except:
					return HttpResponseRedirect('/')
			return redirect('?next=%s' % request.GET['next'])
		else:
			error_username = form['username'].errors.as_text()
			error_pass = form['password'].errors.as_text()

			context = {
				'error_username': error_username, 
				'error_pass': error_pass,
			}

			return render(request, 'home/login_form.html', context)


def login_view(request):
	return render(request, 'home/login_form.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def get_all_tags(request):
	if request.is_ajax():
		try:
			tag = Tag.objects.all()
			data = serializers.serialize('json', tag, fields = {'name'})
			# print(data)
			return HttpResponse(data, content_type='application/json')
		except Exception as e:
			raise e
	else:
		raise Http404