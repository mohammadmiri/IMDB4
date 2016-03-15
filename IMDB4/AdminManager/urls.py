from . import views


from django.conf.urls import url, patterns
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.HomePage, name='homepage'),
    url(r'^pollArchive$', views.PollArchive, name='pollArchive'),
    url(r'^polling/(?P<poll_id>[0-9]+)$', views.Polling, name='polling'),
    url(r'^polling_result/(?P<pollOption_number>[0-9]+)/(?P<poll_id>[0-9]+)', views.Polling_result, name='polling_result')
    ]


