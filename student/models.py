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
    facebook_id = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    """
    Students' school project.
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.name


class Subject(models.Model):
    """
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.name


class Experience(models.Model):
    """
    Student's previous experiences (internship, summer jobs ...)
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    date_start = models.DateField()
    date_end = models.DateField()

    def __unicode__(self):
        return self.name


class Student(models.Model):
    """
    """
    facebook_id = models.CharField(unique=True, max_length=20)
    first_name = models.CharField(max_length=200)
    sur_name = models.CharField(max_length=200)
    school = models.ForeignKey('School', null=True, blank=True)
    experiences = models.ManyToManyField('Experience', null=True, blank=True)
    projects = models.ManyToManyField('Project', null=True, blank=True)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.sur_name)


class Company(models.Model):
    """
    Companies which are looking for applicants
    """
    facebook_id = models.CharField(primary_key=True, max_length=20)
    name        = models.CharField(max_length=200)
  
    def __unicode__(self):
        return self.name


class Internship(models.Model):
    """
    Internship posted by companies.
    """
    company     = models.ForeignKey('Company')
    title       = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    tags        = models.CharField(max_length=200)
    applicants  = models.ManyToManyField('Student')
    active      = models.BooleanField(True)

    def __unicode__(self):
        return self.title
