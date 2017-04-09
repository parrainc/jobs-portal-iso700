from django.conf.urls import url
from .views import IndexView, LoginView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^login/$', LoginView.as_view(), name="login_view"),
]