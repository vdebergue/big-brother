from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404


from forms import *
from models import *


def index(request):
    data = {"title": "Main"}
    return render(request, "main.html", data)

def student_edit(request, pk):
    """
    """
    student = get_object_or_404(Student, pk=pk)
#    import pdb; pdb.set_trace()
    return render_to_response(
        'student/student_edit.html',
        {
            'form': StudentForm(instance=student),
            'student': student,
            },
        context_instance=RequestContext(request))


def student_save(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()  # vuln here, auth + check needed
            return HttpResponseRedirect('/student/' + pk + '/edit')
    else:
        form = StudentForm()

    return HttpResponseRedirect('/student/' + pk + '/edit')


# Create a new company
def add_company(request):
  company = Company.objects.create(name = request['name'])
  return Company.objects.filter('id'=company.id)

# Use Company
def use_company(request):
  return Company.objects.filter('id'=request['company_id'])

# Create a new internship
def create_internship(request):
  internship = Internship.objects.create(title = request['title'], company = Company.objects.filter('id' = request['company']))
  return edit_internship('id'=internship.id)

# View internship data
def view_internship(request):
  return Internship.objects.filter('id' = request['internship'])

# Change fields of the internship
def edit_internship(request):
  internship = Intership.objects.filter('id' = request['internship'])
  if request['title']:
    internship.title = request['title']

  if request['applicants']:
    internship.applicants = request['applicants']

  if request['major']:
    internship.major = request['major']

  internship.save()

# Get students according to search preferences
def get_students(request):
  pass

# view a student profile
def view_student(request):
  pass

# Ona selected internship actions
def ping_students(request):
  pass

# Close an internship having found an intern
def toggle_active(request):
  internship = Internship.objects.filter('id' = request['internship'])
  internship.active = not internship.active
  internship.save()
