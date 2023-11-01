from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')
