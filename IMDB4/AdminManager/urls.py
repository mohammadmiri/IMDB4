from . import views


from django.conf.urls import url, patterns
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.HomePage, name='AdminManager_homepage'),
    url(r'^pollArchive$', views.PollArchive, name='AdminManager_pollArchive'),
    url(r'^polling/(?P<poll_id>[0-9]+)$', views.Polling, name='AdminManager_polling'),
    url(r'^polling_result/(?P<pollOption_number>[0-9]+)/(?P<poll_id>[0-9]+)', views.Polling_result, name='AdminManager_polling_result'),
    url(r'^base/search_suggestion/(?P<value>.*)', views.get_search_result, name='AdminManager_get_result_base'),
    url(r'^news_list/(?P<category>.+)/$', views.show_News_list, name='AdminManager_show_news_list'),
    url(r'^news_list_page/(?P<page>[0-9]+)/(?P<category>[a-zA-Z\\_]+)/$', views.show_news_list_page, name="AdminManager_show_news_list_page" ),
    url(r'^news_text/(?P<news_id>[0-9]+)/$', views.show_news_text, name='AdminManager_show_news_text'),
    ]


