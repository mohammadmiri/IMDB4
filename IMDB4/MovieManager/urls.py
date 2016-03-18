from imdbsite import settings
from . import views


from django.conf.urls import url, patterns
from django.conf.urls.static import static




urlpatterns = [
    url(r'^show/(?P<id>[0-9]+)/$', views.show_movie, name='MovieManager_show_movie'),
    ]


