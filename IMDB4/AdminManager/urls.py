from . import views


from django.conf.urls import url, patterns
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.HomePage, name='homepage'),
    ]


