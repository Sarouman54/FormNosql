"""
Sarah Barrabé
urls.py
src/survey

"""
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('newsurvey', views.new_survey, name="new_survey"),
    path('listsurvey', views.list_survey, name="list_survey"),
    path('listsurvey/update/<str:survey_name>', views.update_survey, name="update_survey"),
    path('listsurvey/delete/<str:survey_name>', views.delete_survey, name="delete_survey"),

    path('survey/<str:survey_name>', views.answer_survey, name="answer_survey"),

    path('signin', views.sign_in, name='sign_in'),
    path('signout', views.sign_out, name='sign_out'),
    path('signup', views.sign_up, name='sign_up')
]