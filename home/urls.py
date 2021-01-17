from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path("",views.index,name='homepage'),
    path("events",views.events,name='eventpage'),
    path("register",views.register,name='formsub'),
    path("team",views.team,name='teampage'),
    path("achievements",views.achievements,name='achievementpage'),
    path("article",views.article,name='articlepage'),
    path("newsletter",views.newsletter,name='newletterpage'),
    path("learning",views.learning,name='peerlearning-page'),
]