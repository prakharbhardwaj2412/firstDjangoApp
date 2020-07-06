from django.conf.urls import url
from . import views

urlpatterns = [
	# /register/
    url(r'^$', views.index, name='index'),

    # /register/71/
    url(r'^(?P<patient_id>[0-9]+)/$', views.detail, name='detail'),
]
