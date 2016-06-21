__author__ = 'mohammad'


from . import views

from django.conf.urls import url, patterns
from django.conf.urls.static import static

urlpatterns = [
    url(r'^login/$', views.login_page, name='UserManager_login'),
    url(r'^signup/$', views.signup_page, name='UserManager_signup'),
    url(r'^showـprofile/(?P<username>[a-zA-Z0-9]+)/$', views.view_profile, name='UserManager_view_profile'),
    url(r'^search_celebrities/(?P<value>.*)/$', views.search_celebrity_sugggestion, name='UserManager_search_celebrity'),
    url(r'^search_movies/(?P<value>.*)/$',views.show_suggestion_search_film,name='UserManager_search_movie'),
    url(r'^make_list/$',views.make_list,name='UserManager_make_list'),
    ]


