from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='portfolios_home'),
    url(r'^(?P<categorie>)$', views.categorie_all, name='potfolio_categorie_all'),
    url(r'^(?P<categorie>)/(?P<index>)$', views.categorie_image, name='portfolio_categorie_image'),
]
