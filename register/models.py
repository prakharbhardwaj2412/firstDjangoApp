from django.db import models
from django.urls import reverse

# Create your models here.

class PatientInfo(models.Model):
	"""docstring for PatientInfo"""
	PATIENT_NAME = models.CharField(max_length=250, default="NULL")
	EMAIL = models.CharField(max_length=250, default="NULL")
	GENDER = models.CharField(max_length=250, default="NULL")
	DOB = models.DateField(max_length=250, default="NULL")
	CONTACT = models.CharField(max_length=20, default="NULL")

	def get_absolute_url(self):
		# return reverse('register:detail', kwargs={'pk': self.pk})
		return reverse('register:index')

	def __str__(self):
		return self.PATIENT_NAME+ ' - '+self.GENDER