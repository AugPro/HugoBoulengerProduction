from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="videos_home"),
    url(r'^(?P<categorie>.+)$', views.by_categorie, name='videos_by_categorie'),
]
