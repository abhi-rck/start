from django.db import models

# Create your models here.
class seeq(models.Model):
    name1=models.CharField(max_length=50)
    name2=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    college=models.TextField()
    mobile=models.CharField(max_length=10)
    def __str__(self):
        return str(self.id)

class alumni(models.Model):
    img=models.ImageField()
    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=10)
    collegeid=models.CharField(max_length=11)
    def __str__(self):
        return str(self.id)

class achievement(models.Model):
    name=models.TextField()
    awardedby=models.TextField()
    issueyear=models.CharField(max_length=4)
    summary=models.TextField()
    def __str__(self):
        return str(self.id)

class articles(models.Model):
    img=models.ImageField(upload_to="articles/")
    heading=models.TextField()
    curatedby=models.CharField(max_length=50)
    date=models.CharField(max_length=50,help_text='Enter date in format 28 March,2020')
    tags=models.CharField(max_length=100,help_text='Energy Polythene')
    summary=models.TextField()
    def __str__(self):
        return str(self.id)

class peerlearning(models.Model):
    video=models.CharField(max_length=500)
    name=models.CharField(max_length=50)
    heading=models.TextField()
    location=models.CharField(max_length=50)
    date=models.CharField(max_length=50,help_text='Enter date in format 28 March,2020')
    tags=models.CharField(max_length=100,help_text='Energy Polythene')
    detail=models.TextField()
    def __str__(self):
        return str(self.id)

class upcomingpeerlearning(models.Model):
    img=models.ImageField(upload_to="upcomingsession/")
    name=models.CharField(max_length=50)
    heading=models.TextField()
    email=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    date=models.CharField(max_length=50,help_text='Enter date in format 28 March,2020')
    tags=models.CharField(max_length=100,help_text='Energy Polythene')
    def __str__(self):
        return str(self.id)


class faculty(models.Model):
    name=models.CharField(max_length=50)
    qualification1=models.CharField(max_length=100)
    qualification2=models.CharField(max_length=100)
    message=models.TextField()
    image=models.ImageField(upload_to="facultys/")
    def __str__(self):
        return str(self.name)

class student(models.Model):
    year=models.IntegerField()
    studentname=models.CharField(max_length=50)
    branchname=models.CharField(max_length=50)
    experience=models.TextField()
    image=models.ImageField(upload_to="students/")
    def __str__(self):
        return str(self.name)

class samplepaper(models.Model):
    pdf=models.FileField(upload_to="samplepapers/")
    title=models.CharField(max_length=50)
    def __str__(self):
        return str(self.title)

class newsletters(models.Model):
    curators=models.CharField(max_length=200,help_text='Names separated by commas:- Abhinav,Neha,Nikhil')
    newsletterpdf=models.FileField(upload_to="newsletters/")
    editionmonth=models.CharField(max_length=200,help_text='Published Month Name:- December')
    def __str__(self):
        return str(self.id)

class eventupdates(models.Model):
    update=models.TextField()
    def __str__(self):
        return str(self.id)
