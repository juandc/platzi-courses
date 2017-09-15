from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.gato, name='gato'),
    url(r'^saludo/', views.saludo, name='gato')
]
