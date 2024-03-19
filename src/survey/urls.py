"""
Sarah Barrabé
urls.py
src/survey

"""
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('newsurvey', views.create_survey, name="create_survey"),

    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup')
]