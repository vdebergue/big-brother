from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi world")

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
  internship.save
