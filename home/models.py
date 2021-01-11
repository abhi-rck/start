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

class suggest(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    suggestion=models.TextField()
    def __str__(self):
        return str(self.id)

class questionpaper(models.Model):
    title=models.CharField(max_length=50)
    files=models.FileField()
    def __str__(self):
        return str(self.id)