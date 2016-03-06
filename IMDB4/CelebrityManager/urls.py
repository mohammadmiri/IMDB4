from . import views


from django.conf.urls import url, patterns




urlpatterns = [
    url(r'^show/(?P<name>.*?)/$', views.show_celebrity, name='show_celebrity'),
    ]





