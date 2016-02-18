from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from django.shortcuts import render

from .models import Question
from .forms import NewProblemForm

def index(request):
  return render(request, 'basics/base_index.html', {})

def add_problem(request):
  if request.method == 'POST':
    newProblemForm = NewProblemForm(request.POST)
    if newProblemForm.is_valid():
      # process data in form.cleaned_data
      formInput = newProblemForm.cleaned_data
      print(formInput)
      newProblem = Question(\
        title=formInput['name'],\
        description=formInput['description'],\
        init_time=datetime.now(),\
        mod_time=datetime.now(),\
        status=False)
      newProblem.save()
      return HttpResponseRedirect('/all_problems')
  else:
    newProblemForm = NewProblemForm()

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
  return render(request, 'basics/all_problems.html', {'problemList': allProblemsExpanded})

def edit_problem(request, suppliedId):
  print("EDIT " + str(suppliedId))
  return render(request, 'basics/edit_problem.html', {'id': suppliedId})

def view_problem(request, suppliedId):
  print ("VIEW " + str(suppliedId))
  return render(request, 'basics/view_problem.html', {'id': suppliedId})
