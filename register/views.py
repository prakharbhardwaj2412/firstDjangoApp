# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import PatientInfo

def index(request):
	all_patients = PatientInfo.objects.all()
	html = ''
	for patient in all_patients:
		url = '/register/' + str(patient.id) + '/'
		html += '<a href="'+ url +'">'+ patient.PATIENT_NAME +'</a><br>'
	return HttpResponse(html)


def detail(request, patient_id):
		return HttpResponse("<h2>details for Patient Id: "+ str(patient_id) +"</h2>")