from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from basics.models import Tag, Question, Choice, Answer, Comment, UserProfile, Class
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .models import Question
from .forms import ProblemForm
from .forms import MULTIPLE_CHOICE
from .forms import FREE_RESPONSE
import re

# DEBUGGING USER -- RUN THIS ONCE
# User.objects.create_user("testuser","test@test.com","testpassword")

# TODO: Restrict users from making questions with the same title,
# since this is used to identify the ajax call that sends the choices

question_choices_to_add = {}


def index(request):
    return render(request, 'basics/base_index.html', {})


def add_problem(request):
    if request.method == 'POST':
        newProblemForm = ProblemForm(request.POST)
        if newProblemForm.is_valid():
            # process data in form.cleaned_data
            formInput = newProblemForm.cleaned_data
            print(formInput)

            if formInput['problemType'] == MULTIPLE_CHOICE:
                newProblem = Question( \
                    title=formInput['title'], \
                    description=formInput['description'], \
                    problemType=formInput['problemType'], \
                    # choices=formInput['choices'],\
                    init_time=datetime.now(), \
                    mod_time=datetime.now(), \
                    status=False)

                newProblem.save()
                newProblem.contributer.add(request.user)
                newProblem.save()

                if formInput['title'] in question_choices_to_add:
                    for choice in question_choices_to_add[formInput['title']]:
                        newChoice = Choice( \
                            question=newProblem, \
                            choice_text=choice['text'], \
                            correctness=choice['correctness'])
                        newChoice.save();

                print(Choice.objects.filter(question=newProblem))

                # return HttpResponseRedirect('/all_problems')
            elif formInput['problemType'] == FREE_RESPONSE:
                newProblem = Question( \
                    title=formInput['title'], \
                    description=formInput['description'], \
                    problemType=formInput['problemType'], \
 \
                    init_time=datetime.now(), \
                    mod_time=datetime.now(), \
                    status=False)
                # print(request)
                # print(request.user)
                newProblem.save()
                newProblem.contributer.add(request.user)
                newProblem.save()
                # return HttpResponseRedirect('/all_problems')

            else:
                print("Unrecognized question problemType " + formInput['problemType'])

            return HttpResponseRedirect('/all_problems')
    else:
        newProblemForm = ProblemForm()

    return render(request, 'basics/add_problem.html', {'formVar': newProblemForm})


def queue_add_problem_choices(request):
    if request.method == 'POST':
        choices_dict = request.POST.dict()
        # print(list(request.POST.lists()))
        print(choices_dict)

        temp_dict = {}

        for key in choices_dict:
            match_obj = re.match('.+\[(\d+)\]\[(.+)\]', key)
            if match_obj:
                # print(matchObj.group(1))
                # print(matchObj.group(2))
                choice_number = match_obj.group(1)
                field = match_obj.group(2)
                value = choices_dict[key]

                if field == 'correctness':
                    if value == 'true':
                        value = True
                    else:
                        value = False
                # print(field, value)
                if choice_number not in temp_dict:
                    temp_dict[choice_number] = {'text': '', 'correctness': ''}
                temp_dict[choice_number][field] = value
            else:
                print("key '" + key + "' did not match regexp")

        temp_list = [{} for key in temp_dict]
        for key in temp_dict:
            temp_list[int(key)] = temp_dict[key]

        print(temp_dict)
        print(temp_list)
        question_choices_to_add[choices_dict['title']] = temp_list[::1]
        # TODO: push temp_dict into choices_to_add,
        # and then add Choice objects inside add_problem

        # print(Question.objects.filter(title=choices_dict['title']))
        return HttpResponse("success")
    return HttpResponse("failure")


def expandProblem(p):
    return { \
        'id': p.id, \
        'title': p.title, \
        'description': p.description, \
        'init_time': p.init_time, \
        'mod_time': p.mod_time, \
        'view_link': '/problem/view/' + str(p.id), \
        'edit_link': '/problem/edit/' + str(p.id) \
        }


def all_problems(request):
    allProblems = Question.objects.all()
    allProblemsExpanded = [expandProblem(p) for p in allProblems]
    # print(allProblemsExpanded)
    return render(request, 'basics/all_problems.html', {'problemList': allProblemsExpanded})


def edit_problem(request, suppliedId):
    problem = Question.objects.get(pk=suppliedId)
    currProblemForm = ProblemForm({'title': problem.title, 'description': problem.description})

    if request.method == 'POST':
        updatedProblemForm = ProblemForm(request.POST)
        if updatedProblemForm.is_valid():
            # process data in form.cleaned_data
            formInput = updatedProblemForm.cleaned_data
            print(formInput)
            problem.title = formInput['title']
            problem.description = formInput['description']
            problem.mod_time = datetime.now()
            problem.author.add(request.user)
            problem.save()
            return HttpResponseRedirect('/all_problems')

    return render(request, 'basics/edit_problem.html', {'id': suppliedId, 'formVar': currProblemForm})


def view_problem(request, suppliedId):
    problem = Question.objects.get(pk=suppliedId)
    currProblemValues = {'title': problem.title, 'description': problem.description}
    currProblemChoices = Choice.objects.filter(question=Question.objects.get(title=problem.title))
    print(currProblemValues)
    print(currProblemChoices)

    return render(request, 'basics/view_problem.html',
                  {'id': suppliedId, 'fields': currProblemValues, 'choices': currProblemChoices})


@login_required(redirect_field_name='home')
def home(request):
     userprofile = UserProfile.objects.filter(user = request.user.id)
     allProblems = Question.objects.all()
     allProblemsExpanded = [expandProblem(p) for p in allProblems]
     return render(request, 'basics/home.html', {'userprofile': userprofile, 'problemList':allProblemsExpanded})

@login_required(redirect_field_name='home')
def user_profile(request):
    userprofile = UserProfile.objects.filter(user=request.user.id)
    user = request.user
    questions = user.question_set.all().order_by('-mod_time')
    answers = user.answer_set.all().order_by('-mod_time')
    comments = user.comment_set.all().order_by('-mod_time')
    classes = Class.objects.filter(student=request.user.id)
    context = {'userprofile': userprofile, 'questions': questions,
               'answers': answers, 'comments': comments, 'classes': classes, 'user': user}
    return render(request, 'basics/user_profile.html', context)


@login_required(redirect_field_name='home')
def user_setting(request):
    userprofile = UserProfile.objects.filter(user=request.user.id)
    user = request.user
    questions = user.question_set.all().order_by('-mod_time')
    answers = user.answer_set.all().order_by('-mod_time')
    comments = user.comment_set.all().order_by('-mod_time')
    classes = Class.objects.filter(student=request.user.id)
    context = {'userprofile': userprofile, 'questions': questions,
               'answers': answers, 'comments': comments, 'classes': classes, 'user': user}
    return render(request, 'basics/user_setting.html', context)

# search - navigation bar search request
def search(request):
    # Get the text from user input and parse it to list
    searchContent = request.GET.get('search_text').lower()
    searchTextList = searchContent.split()

    # Search questions based on the title and user keywords
    problems = []
    for text in searchTextList:
        problems += (Question.objects.filter(title__contains=text))
    problems = set(problems)
    problems = [expandProblem(p) for p in problems]
    return render(request, 'basics/search.html', {'problems': problems, 'query': searchContent})
