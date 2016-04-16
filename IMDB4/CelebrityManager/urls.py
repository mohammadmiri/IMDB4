from . import views


from django.conf.urls import url, patterns




urlpatterns = [
    url(r'^show/(?P<id>[0-9]+?)/$', views.show_celebrity, name='show_celebrity'),
    url(r'^show_awards/(?P<id>[0-9]+)/$', views.get_awards_celebrity, name='show_celebrity_awards')
    ]





