from . import views


from django.conf.urls import url, patterns
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.HomePage, name='homepage'),
    url(r'^pollArchive$', views.PollArchive, name='pollArchive'),
    url(r'^polling/(?P<poll_id>[0-9]+)$', views.Polling, name='polling'),
    url(r'^polling_result/(?P<pollOption_number>[0-9]+)/(?P<poll_id>[0-9]+)', views.Polling_result, name='polling_result'),
    url(r'^base/search_suggestion/(?P<value>.*)', views.get_search_result, name='get_result_base'),
    url(r'^news_list/(?P<category>.+)/$', views.show_News_list, name='show_news_list'),


    url(r'^test/$',views.test,name='test'),
    url(r'^test_filter/$', views.test_filter, name='test_filter'),
    ]


