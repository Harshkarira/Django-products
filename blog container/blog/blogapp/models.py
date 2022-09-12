from operator import truediv
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    datePosted = models.DateTimeField(null=True) #we have to give null true bcuz default is false and we have to give something in paranthesis
    # personID = models.ForeignKey(Person,on_delete=models.CASCADE,default=1)

class Person(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
