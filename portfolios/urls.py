from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='stills_home'),
    url(r'^(?P<categorie>)$', views.categorie_all, name='stills_categorie_all'),
    url(r'^(?P<categorie>)/(?P<index>)$', views.categorie_image, name='stills_categorie_image'),
]
