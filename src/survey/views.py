from django.shortcuts import render
from .models import survey_collection
from django.http import HttpResponse

def home_index(request):
    return render(request, "survey/index.html")

def add_survey(request):
    survey = {
        "name": "Sondage préférences alimentaires"
    }
    survey_collection.insert_one(survey)
    return HttpResponse("New sondage is added")