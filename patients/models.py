from django.db import models

# Create your models here.


class PatientTable(models.Model):
	"""docstring for PatientInfo"""
	PATIENT_NAME = models.CharField(max_length=250, default="NULL")
	EMAIL = models.CharField(max_length=250, default="NULL")
	GENDER = models.CharField(max_length=250, default="NULL")
	DOB = models.CharField(max_length=250, default="2000-23-11")
	CONTACT = models.CharField(max_length=20, default="NULL")


	
	def __str__(self):
		return self.PATIENT_NAME+ ' - '+self.EMAIL