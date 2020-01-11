from django.conf.urls import include, url
from . import views

app_name = 'music'
urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),
    # /music/<id>
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='index-detail'),
    # /music/<album_id>/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='index-favorite'),
]

