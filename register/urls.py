from django.conf.urls import url
from . import views

app_name = 'register'

urlpatterns = [

	# /register/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /register/71/
    url(r'^(?P<patient_id>[0-9]+)/$', views.detail, name='detail'),

    # /register/add
    url(r'add/$', views.PatientCreate.as_view(), name='patient-add'),

    # /register/patient/2
    url(r'patient/(?P<pk>[0-9]+)/$', views.PatientUpdate.as_view(), name='patient-update'),

    # /register/patient/2/delete
    url(r'patient/(?P<pk>[0-9]+)/delete/$', views.PatientDelete.as_view(), name='patient-delete'),

]
