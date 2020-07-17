from django.conf.urls import url

from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^(?P<patient_id>[0-9]+)/$', views.read, name='read'),

    url('new', views.create, name='create'),

    url('store', views.store, name='store'),
    

    url(r'^(?P<patient_id>[0-9]+)/update/$', views.update, name='update'),

    url(r'^(?P<patient_id>[0-9]+)/updated/', views.updated, name='updated'),


]