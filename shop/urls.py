from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='shop_home'),
    url(r'^(?P<index>.+)$', views.image, name='shop_image'),
]
