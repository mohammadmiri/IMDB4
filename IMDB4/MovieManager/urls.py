from imdbsite import settings
from . import views


from django.conf.urls import url, patterns
from django.conf.urls.static import static




urlpatterns = [
    url(r'^show/(?P<id>[0-9]+)/$', views.show_movie, name='MovieManager_show_movie'),
    url(r'^show_awards/(?P<id>[0-9]+)/$', views.show_award_movie, name='MovieManager_show_awards'),
    url(r'^show_top_100/$', views.get_100_best_movies, name='MovieManager_top_100'),
    url(r'^sale_table/$',views.sale_table,name='MovieManager_sale_table'),
    url(r'^festivals/$',views.search_festival_awards,name='MovieManager_search_festival'),
    url(r'^all_crew/(?P<id>[0-9]+)/$', views.all_crew, name='MovieManager_all_crew'),
    ]


