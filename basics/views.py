from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from basics.models import Tag, Question, Choice, Answer, Comment, UserProfile, Class
from django.shortcuts import render
from django.contrib.auth.models import User, Group

from .models import Question
from .forms import ProblemForm

def index(request):
  return render(request, 'basics/base_index.html', {})

def add_problem(request):
  if request.method == 'POST':
    newProblemForm = ProblemForm(request.POST)
    if newProblemForm.is_valid():
      # process data in form.cleaned_data
      formInput = newProblemForm.cleaned_data
      print(formInput)
      newProblem = Question(\
        title=formInput['title'],\
        description=formInput['description'],\
        init_time=datetime.now(),\
        mod_time=datetime.now(),\
        status=False)
      newProblem.save()
      return HttpResponseRedirect('/all_problems')
  else:
    newProblemForm = ProblemForm()

  return render(request, 'basics/add_problem.html', {'formVar': newProblemForm})

def expandProblem(p):
  return {\
    'id':p.id,\
    'title':p.title,\
    'description':p.description,\
    'init_time':p.init_time,\
    'mod_time':p.mod_time,\
    'view_link':'/problem/view/' + str(p.id),\
    'edit_link':'/problem/edit/' + str(p.id)\
  }

def all_problems(request):
  allProblems = Question.objects.all()
  allProblemsExpanded = [expandProblem(p) for p in allProblems]
  print(allProblemsExpanded)
  return render(request, 'basics/all_problems.html', {'problemList': allProblemsExpanded})

def edit_problem(request, suppliedId):
  # print("EDIT " + str(suppliedId))
  problem = Question.objects.get(pk=suppliedId)
  currProblemForm = ProblemForm({'title':problem.title, 'description':problem.description})
  
  if request.method == 'POST':
    updatedProblemForm = ProblemForm(request.POST)
    if updatedProblemForm.is_valid():
      # process data in form.cleaned_data
      formInput = updatedProblemForm.cleaned_data
      print(formInput)
      problem.title = formInput['title']
      problem.description = formInput['description']
      problem.mod_time = datetime.now()
      problem.save()
      return HttpResponseRedirect('/all_problems')

  return render(request, 'basics/edit_problem.html', {'id': suppliedId, 'formVar': currProblemForm})

def view_problem(request, suppliedId):
  # print ("VIEW " + str(suppliedId))
  problem = Question.objects.get(pk=suppliedId)
  currProblemValues = {'title':problem.title, 'description':problem.description}
  print(currProblemValues)

  return render(request, 'basics/view_problem.html', {'id': suppliedId, 'fields': currProblemValues})

def home(request, username):
     userprofile = UserProfile.objects.get(user__exact = username)
     #classes_enrolled = Class.objects.filter()
     return HttpResponse("This worked")
