from django.db import models

# Create your models here.

class App(models.Model):
    """
    """
    secret = models.CharField(max_length=32)
    app_id = models.IntegerField()

class School(models.Model):
    """
    """
    facebook_id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=200)

class Project(models.Model):
    """
    Students' school project.
    """
    name = models.CharField(max_length=200)

class Subject(models.Model):
    """
    """
    name = models.CharField(max_length=200)

class Experience(models.Model):
    """
    Student's previous experiences (internship, summer jobs ...)
    """
    name = models.CharField(max_length=200)
    date_start = models.DateField()
    date_end = models.DateField()

class Student(models.Model):
    """
    """
    facebook_id = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=200)
    sur_name = models.CharField(max_length=200)
    school = models.ForeignKey('School')
    experiences = models.ForeignKey('Experience')
    projects = models.ManyToManyField('Project')


class Company(models.Model):
    """
    Companies which are looking for applicants
    """
    facebook_id = models.CharField(primary_key=True, max_length=20)
    name        = models.CharField(max_length=200)
  
class Internship(models.Model):
    """
    Internship posted by companies.
    """
    name = models.CharField(max_length=200)
    company = models.ForeignKey('Company')
    applicants = models.ManyToManyField('Student')
    active     = models.BooleanField(True)
