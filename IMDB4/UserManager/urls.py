__author__ = 'mohammad'


from . import views

from django.conf.urls import url, patterns
from django.conf.urls.static import static

urlpatterns = [
    url(r'^login/$', views.login_page, name='login'),
    url(r'^signup/$', views.signup_page, name='signup'),
    url(r'^showProfile/(?P<username>[a-zA-Z0-9]+)/$', views.view_profile, name='view_profile'),
    ]


