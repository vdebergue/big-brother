from django.forms import ModelForm

from student.models import Student, Company, Internship


class StudentForm(ModelForm):
    class Meta:
        model = Student

class CompanyForm(ModelForm):
    class Meta:
        model = Company

class InternshipForm(ModelForm):
    class Meta:
        model = Internship

