from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import seeq,alumni,achievement,articles,peerlearning,upcomingpeerlearning,student,faculty,samplepaper,newsletters,eventupdates
from django.contrib import messages

# Create your views here.
def index(request):
    article=articles.objects.all()[0:2]
    return render(request,'index.html',{'articles':article})

def events(request):
    eventupdate=eventupdates.objects.all().order_by('-id')
    samplepapers=samplepaper.objects.all()
    return render(request,'events.html',{'samplepapers':samplepapers,'eventupdates':eventupdate})

def register(request):
    if request.method == "POST":
        name1=request.POST['name1']
        name2=request.POST['name2']
        email=request.POST['email']
        college=request.POST['college']
        mobile=request.POST['phone']
        new=seeq(name1=name1,name2=name2,email=email,college=college,mobile=mobile)
        new.save()
        messages.info(request,f"Your team have been registered now. Kindly remember the id for future refrences. SEEQ-2021-{new.id}")
        return redirect("/events")

def learning(request):
    learningsession=peerlearning.objects.all()
    upcominglearningsession=upcomingpeerlearning.objects.all()
    return render(request,'learning.html',{'sessions':learningsession,'upcoming':upcominglearningsession})

def article(request):
    article=articles.objects.all().order_by('-id')
    recentarticles=article[:5]
    return render(request,'article.html',{'articles':article,'recentarticles':recentarticles})

def achievements(request):
    awards=achievement.objects.all().order_by('-issueyear')
    return render(request,'achievements.html',{'awards':awards})

def alumnis(request):
    alumnis=alumni.objects.all()
    return render(request,'alumni.html',{'alumnis':alumnis})

def team(request):
    fourthyear=student.objects.all().filter(year=4)
    thirdyear=student.objects.all().filter(year=3)
    secondyear=student.objects.all().filter(year=2)
    facultys=faculty.objects.all()
    return render(request,'team.html',{'fourthyearstudents':fourthyear,'thirdyearstudents':thirdyear,'secondyearstudents':secondyear,'facultys':facultys})

def newsletter(request):
    newsletterdetails=newsletters.objects.all().order_by('-id')
    return render(request,'newsletter.html',{'newsletters':newsletterdetails})

def visit(request):
    return render(request,'visit.html')
