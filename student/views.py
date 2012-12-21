import json

from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404


from forms import *
from models import *


def index(request):
    data = {"title": "Main"}
    return render(request, "main.html", data)


def student_create(request):
    """
    """
    return render_to_response(
        'student/student_create.html',
        context_instance=RequestContext(request))


def student_save(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            student = Student.objects.get(pk=request.POST['id'])
            form = StudentForm(request.POST, instance=student)
        else:
            form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()  # vuln here, auth + check needed
            return HttpResponseRedirect('/student/' + str(student.id))

        return render_to_response(
            'student/student_create.html',
            {'errors': reduce(list.__add__, form.errors.values()),},
            context_instance=RequestContext(request))


def get_student_experiences(request, fb_id):
    """
    Ajax call: get the list of experiences
    """
    student = get_object_or_404(Student, facebook_id=fb_id)
    experiences = [exp.name for exp in student.experiences.all()]
    return HttpResponse(json.dumps(experiences), mimetype='application/json')


def get_student_projects(request, fb_id):
    """
    Ajax call: get the list of projects
    """
    student = get_object_or_404(Student, facebook_id=fb_id)
    projects = [p.name for exp in student.projects.all()]
    return HttpResponse(json.dumps(projects), mimetype='application/json')


# Create a new company
#def company_create(request):
#  company = Company.objects.create(name = request['name'])
#  return Company.objects.filter('id'=company.id)

def company_edit(request, pk):
    """
    """
    student = get_object_or_404(Company, facebook_id=pk)
#    import pdb; pdb.set_trace()
    return render_to_response(
        'company/company_edit.html',
        {
            'form': CompanyForm(instance=company),
            'company': company,
            },
        context_instance=RequestContext(request))
        
def company_save(request, pk):
    if request.method == 'POST':
        company = Company.objects.get(facebook_id=pk)
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()  # vuln here, auth + check needed
            return HttpResponseRedirect('/company/' + pk + '/edit')
    else:
        form = CompanyForm()

    return HttpResponseRedirect('/company/' + pk + '/edit')

# Create a new internship
def internship_create(request, pk):
  return HttpResponseRedirect('/company/' + pk + '/internship/1/edit')
#  internship = Internship.objects.create(title = request['title'], company = Company.objects.filter('id' = request['company']))
#  return edit_internship('id'=internship.id)

#  return HttpResponseRedirect('/company/' + internship.company.facebook_id + '/internship/' + internship.id + '/edit')

# View / Edit internship data

def internship_edit(request, pk,  internship_id=None):
    """
    """
    internship = get_object_or_404(Internship, id=internship_id)
#    import pdb; pdb.set_trace()
    return render_to_response(
        'company/internship_edit.html',
        {
            'form': InternshipForm(instance=internship),
            'internship': internship,
            },
        context_instance=RequestContext(request))
        
def internship_save(request, internship_id):
    if request.method == 'POST':
        internship = Internship.objects.get(id=internship_id)
        form = InternshipForm(request.POST, instance=internship)
        if form.is_valid():
            form.save()  # vuln here, auth + check needed
            return HttpResponseRedirect('/company/' + internship.company.facebook_id + '/internship/' + internship_id + '/edit')
    else:
        form = CompanyForm()

    return HttpResponseRedirect('/company/' + internship.company.facebook_id + '/internship/' + internship_id + '/edit')

# Get students according to search preferences
def get_students(request):
  pass

# view a student profile
def view_student(request):
  pass

# Ona selected internship actions
def ping_students(request):
  pass


