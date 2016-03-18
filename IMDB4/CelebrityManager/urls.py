from . import views


from django.conf.urls import url, patterns




urlpatterns = [
    url(r'^show/(?P<id>.*?)/$', views.show_celebrity, name='show_celebrity'),
    ]





