from django.conf.urls import url
from .views import IndexView, LoginView, get_all_tags

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^login/$', LoginView.as_view(), name="login_view"),
    url(r'^get-tags/$', get_all_tags, name="get_all_tags"),
]