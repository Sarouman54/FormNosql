"""
Sarah Barrabé
views.py
src/survey

"""
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from db_connection import collection_survey, collection_response

def index(request):
    surveys = collection_survey.find()
    context = {"surveys": surveys}
    return render(request, "./survey/index.html", context)

def new_survey(request):
    if request.method == "POST":
        surveyName = request.POST['namesurvey']
        # question1 = request.POST['question1']
        nbQuestion = request.POST['nb_question']
        creatorEmail = request.user.email
        creatorName = request.user.username
        if collection_survey.find_one({'name': surveyName}):
            print("non")
        else:
            i = 1
            questions = []
            while i <= int(nbQuestion) :
                questions.append({'name': request.POST['question'+str(i)], 'type': request.POST['type'+str(i)]})
                i = i+1
            collection_survey.insert_one({'name': surveyName, 'nb_question': nbQuestion, 'questions': questions, 'user': {'email': creatorEmail, 'username': creatorName}})
            return redirect('list_survey')
    return render(request, "./survey/new_survey.html")

def list_survey(request):
    userName = request.user.username
    userSurvey = collection_survey.find({'user.username': userName})
    context = {"surveys": userSurvey}
    return render(request, "./survey/list_survey.html", context)

def delete_survey(request, survey_name):
    collection_survey.delete_one({'name': survey_name})
    return redirect('list_survey')

def update_survey(request, survey_name):
    survey = collection_survey.find_one({'name': survey_name})
    questions = survey['questions']
    # print(questions['name'])
    context = {"survey": survey, "questions": questions}
    if request.method == "POST":
        i = 0
        questions = []
        while i < int(survey['nb_question']):
            questions.append({'name': request.POST['question_'+str((i+1))], 'type': request.POST['type'+str((i+1))]})
            i = i+1
        collection_survey.update_one({'name': survey_name}, {'$set': {'questions': questions}})
        return redirect('list_survey')
    return render(request, "./survey/update_survey.html", context)

def answer_survey(request, survey_name):
    survey = collection_survey.find_one({'name': survey_name})
    context = {"survey": survey}
    print()
    if request.method == "POST":
        userName = request.user.username
        userEmail = request.user.email
        i = 0
        responses = []
        while i < int(survey['nb_question']):
            responses.append({'question': survey['questions'][i]['name'], 'response': request.POST['response_'+str((i+1))]})
            i = i+1
        collection_response.insert_one({'sondage': {'id': survey['_id'], 'name': survey['name']}, 'user': {'email': userEmail, 'username': userName}, 'response': responses})
    return render(request, "./survey/answer_survey.html", context)

def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, 'Votre compte a été créé avec succès')
        return redirect('sign_in')
    return render(request, "./registration/sign_up.html")

def sign_in(request):
    if request.method == "POST":
        # email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(email)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "./survey/index.html")
        else:
            messages.error(request, 'Votre mot de passe ou votre email est incorrect')
            return redirect('sign_in')
    return render(request, "./registration/sign_in.html")

def sign_out(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté')
    return redirect ('index')