# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(requests):
	return HttpResponse("<h1>This is the Registration Page</h1><h1>Registration</h1>")