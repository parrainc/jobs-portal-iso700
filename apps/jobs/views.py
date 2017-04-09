import json
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.core import serializers
from django.http import HttpResponse, Http404
from .models import Job, Tag
from .forms import CreateJobsForm


class JobsListView(ListView):
	model = Job
	context_object_name = 'jobs'

	def get_context_data(self, **kwargs):
		context = super(JobsListView, self).get_context_data(**kwargs)
		context['tags'] = Tag.objects.all()
		return context


class JobsCreateView(CreateView):
	model = Job
	form_class = CreateJobsForm
	success_url = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(JobsCreateView, self).form_valid(form)

	def form_invalid(self, form):
		return super(JobsCreateView, self).form_invalid(form)


class JobDetailView(DetailView):
	model = Job
	context_object_name = 'job'

	def get_context_data(self, **kwargs):
		context = super(JobDetailView, self).get_context_data(**kwargs)
		return context



def BuscarAjax(request):
	if request.is_ajax():

		tag = Tag.objects.get(id = request.GET['id'])
		jobs = Job.objects.filter(tag = tag)

		data = serializers.serialize(
				'json', 
				jobs, 
				fields= {
						'title', 
						'description', 
						'modified', 
						'slug'
						}
		)
		# print(data)
		return HttpResponse(data, content_type='application/json')
	else:
		raise Http404
