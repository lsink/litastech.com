from django.shortcuts import render

from .models import Projects

# Create your views here.

def home(request):
	all_projects = Projects.objects.all()
	return render(request, 'home.html', {'projects': all_projects})
