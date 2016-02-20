from django.shortcuts import render
from django.contrib.auth.models import User, Group

from .models import Question

def index(request):
     return render(request, 'basics/base_index.html', {})
