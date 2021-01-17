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
    img=models.ImageField()
    heading=models.TextField()
    curatedby=models.CharField(max_length=50)
    date=models.CharField(max_length=50,help_text='Enter date in format 28 March,2020')
    tags=models.CharField(max_length=100,help_text='Energy Polythene')
    summary=models.TextField()
    def __str__(self):
        return str(self.id)    