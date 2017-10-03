from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='shop_home'),
    url(r'^payment/(?P<key>.+)$', views.payment, name='shop_payment'),
    url(r'^(?P<key>.+)$', views.image, name='shop_image'),
]
