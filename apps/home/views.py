from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, View
from django.http import HttpResponseRedirect

# from apps.home.models import *
# from .forms import LoginForm
# Create your views here.

class IndexView(ListView):
	template_name = 'home/index.html'
	# queryset = Question.objects.all().order_by('-created')[:4]

	def get_queryset(self):
		#queryset = Question.objects.all().order_by('-created')[:4]
		#tags = [ question.tag.all() for question in queryset]
		return ""


class LoginView(View):
	
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return render(request, 'home/login_form.html')
		else:
			return redirect('/')

	def post(self, request, *args, **kwargs):
		# logout(request)

		# if request.POST:
		# 	username = request.POST['username']
		# 	password = request.POST['password']
		# 	user = authenticate(
		# 		username = username, 
		# 		password = password
		# 	)
		# 	if user is not None:
		# 		login(request, user)
		# 		return HttpResponseRedirect(request.GET['next'])
		# 	return redirect('?next=%s' % request.GET['next'])
		# else:
		# 	error_username = form['username'].errors.as_text()
		# 	error_pass = form['password'].errors.as_text()

		# 	context = {
		# 		'error_username': error_username, 
		# 		'error_pass': error_pass,
		# 	}

			return render(request, 'home/login_form.html', context)


def login_view(request):
	return render(request, 'home/login_form.html')