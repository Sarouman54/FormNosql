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
from db_connection import collection_survey, collection_response, collection_question, collection_user

def index(request):
    surveys = collection_survey.find()
    context = {"surveys": surveys}
    return render(request, "./survey/index.html", context)

def create_survey(request):
    
    return render(request, "./survey/create_survey.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, 'Votre compte a été créé avec succès')
        return redirect('signin')
    return render(request, "./registration/signup.html")

def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, "./survey/index.html")
        else:
            messages.error(request, 'Votre mot de passe ou votre email est incorrect')
            return redirect('signin')
    return render(request, "./registration/signin.html")

def signout(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté')
    return redirect ('index')