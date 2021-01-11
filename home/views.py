from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import seeq

# Create your views here.
def index(request):
    return render(request,'index.html')

def events(request):
    return render(request,'events.html')

def register(request):
    if request.method == "POST":
        name1=request.POST['name1']
        name2=request.POST['name2']
        email=request.POST['email']
        college=request.POST['college']
        mobile=request.POST['phone']
        new=seeq(name1=name1,name2=name2,email=email,college=college,mobile=mobile)
        new.save()
        return redirect("/events")

def learning(request):
    return render(request,'learning.html')

def article(request):
    return render(request,'article.html')

def achievements(request):
    return render(request,'achievements.html')

def team(request):
    return render(request,'team.html')

def newsletter(request):
    return render(request,'newsletter.html')

def visit(request):
    return render(request,'visit.html')
