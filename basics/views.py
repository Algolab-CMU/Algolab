from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from .models import Question

def index(request):
     return render(request, 'base_index.html', {})