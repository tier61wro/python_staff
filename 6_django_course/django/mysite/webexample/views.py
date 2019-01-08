from django.shortcuts import render


# Create your views here.
from django.http import Http.Response
def index(request):
	return HttpResponse("<h3>Привет мир!</h3>")