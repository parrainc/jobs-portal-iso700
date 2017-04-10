from django.conf.urls import url
from .views import (
	JobsListView, 
	JobsCreateView,
	JobDetailView,
	PostJob,
	SearchJobs)


urlpatterns = [
    url(r'^jobs/$', JobsListView.as_view(), name='jobs'),
    url(r'^jobs/create/$', JobsCreateView.as_view(), name='create_job'),
    url(r'^jobs/(?P<slug>[-\w]+)/$', JobDetailView.as_view(), name='detail_job'),
    url(r'^search-jobs/$', SearchJobs, name='search_jobs'),
    url(r'^post-job/$', PostJob, name='post_job'),
]