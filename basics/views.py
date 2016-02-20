from django.shortcuts import render
from django.http import HttpResponse
from basics.models import Tag, Question, Choice, Answer, Comment, UserProfile,
Class
# Create your views here.

from django.shortcuts import render

from .models import Question

def index(request):
     return render(request, 'basics/base_index.html', {})

def home(request, username):
     userprofile = UserProfile.objects.get(user__exact = username)
     #classes_enrolled = Class.objects.filter()
     return HttpResponse("This worked")
