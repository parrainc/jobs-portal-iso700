from django.conf.urls import url
from .views import (
	JobsListView, 
	JobsCreateView,
	JobDetailView)


urlpatterns = [
    url(r'^jobs/$', JobsListView.as_view(), name='jobs'),
    url(r'^jobs/create/$', JobsCreateView.as_view(), name='create_job'),
    url(r'^jobs/(?P<slug>[-\w]+)/$', JobDetailView.as_view(), name='detail_job'),
    # url(r'^buscar-ajax/$', 'apps.jobs.views.BuscarAjax', name='buscar_ajax'),
]