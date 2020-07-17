# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
import pdb

from .models import PatientTable


def index(request):
    patient_list = PatientTable.objects.all()
    # return HttpResponse(patient_list, request)
    template = loader.get_template('patients/index.html')
    context = {
        'patient_list': patient_list,
    }
    return HttpResponse(template.render(context, request))


def read(request, patient_id):
	# return HttpResponse(patient_id, request)
	print(patient_id)
	patient_detail = PatientTable.objects.get(pk=patient_id)
	# return HttpResponse(patient, request)
	# print(patient)
	
	template = loader.get_template('patients/read.html')
	return HttpResponse(template.render({'patient': patient_detail}, request))

def update(request, patient_id):
	patient = PatientTable.objects.get(pk=patient_id)
	template = loader.get_template('patients/update.html')
	print("hello")
	return HttpResponse(template.render({'patient': patient}, request))


def updated(request, patient_id):
	old = PatientTable.objects.get(pk=patient_id)
	print (old)
	# # updated = old.objects.get(pk=request.POST['patient'])
	# print(updated)
	# updated.PATIENT_NAME = patient.PATIENT_NAME
	# updated.EMAIL = patient.EMAIL
	# updated.GENDER = patient.GENDER
	# updated.DOB = patient.DOB 
	# updated.CONTACT = patient.CONTACT 

	# updated.save()

	# return HttpResponseRedirect(reverse('patients:read', args=(old.id,)))

def create(request):
	template = loader.get_template('patients/create.html')
	return HttpResponse(template.render({'': ''}, request))


def store(request):
	print('##################')
	print(request.method)
	print(request.body)
	print(request.POST)
	print(request.POST['Pname'])
	print('$$$$$$$$$$$$$$$$$$$$$$$')
	info= PatientTable(PATIENT_NAME=request.POST['Pname'], EMAIL=request.POST['Pemail'], GENDER=request.POST['Pgender'], DOB=request.POST['Pdob'], CONTACT=request.POST['Pcontact'])
	info.save()
	return HttpResponseRedirect('/patient')
