from imdbsite import settings
from . import views


from django.conf.urls import url, patterns
from django.conf.urls.static import static




urlpatterns = [
    url(r'^show/(?P<id>[0-9]+)/$', views.show_movie, name='MovieManager_show_movie'),
    url(r'^show_awards/(?P<id>[0-9]+)/$', views.show_award_movie, name='MovieManager_show_awards'),
    url(r'^show_top_100/$', views.get_100_best_movies, name='MovieManager_top_100'),
    ]


