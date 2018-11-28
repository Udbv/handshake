from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^networks/$', views.NetworkListView.as_view(), name='networks'),
]