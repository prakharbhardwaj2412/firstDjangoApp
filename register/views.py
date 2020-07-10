# from django.shortcuts import render

# Create your views here.

# from django.http import Http404
# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import PatientInfo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# from .models import PatientInfo

# def index(request):
# 	all_patients = PatientInfo.objects.all()
	# html = ''
	# for patient in all_patients:
	# 	url = '/register/' + str(patient.id) + '/'
	# 	html += '<a href="'+ url +'">'+ patient.PATIENT_NAME +'</a><br>'
	# template = loader.get_template('register/index.html')
	# context = {'all_patients': all_patients}
	# return HttpResponse(template.render(context, request))
	# return render(request, 'register/index.html', {'all_patients': all_patients})

def detail(request, patient_id):
		# return HttpResponse("<h2>details for Patient Id: "+ str(patient_id) +"</h2>")
		# try:
		# 	patient = PatientInfo.objects.get(pk=patient_id)
		# except PatientInfo.DoesNotExist:
		# 	raise Http404("Patient does not exist")
		# patient = PatientInfo.objects.get(pk=patient_id)
		patient = get_object_or_404(PatientInfo, pk=patient_id)
		return render(request, 'register/detail.html', {'patient': patient})

class IndexView(generic.ListView):
	template_name = 'register/index.html'
	context_object_name = 'all_patients'

	def get_queryset(self):
		return PatientInfo.objects.all()

# class DetailView(generic.DetailView):
	"""docstring for DetailView"""
	# model = PatientInfo
	# patient = PatientInfo.objects.get(pk=patient_id)
	# template_name = 'register/detail.html'

class PatientCreate(CreateView):
	"""docstring for PatientCreate"""
	model = PatientInfo
	fields = ['PATIENT_NAME', 'EMAIL', 'GENDER', 'DOB', 'CONTACT']
	
class PatientUpdate(UpdateView):
	"""docstring for PatientUpdate"""
	model = PatientInfo
	fields = ['PATIENT_NAME', 'EMAIL', 'GENDER', 'DOB', 'CONTACT']
	
class PatientDelete(DeleteView):
	"""docstring for PatientDelete"""
	model = PatientInfo
	success_url = reverse_lazy('register:index')