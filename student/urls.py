from django.views.generic import DetailView, ListView
from django.conf.urls import patterns, include, url

from student.models import Student
from student.models import Company
from student.models import Internship

urlpatterns = patterns('',
    # student urls
    url(r'^$',
        ListView.as_view(
            queryset=Student.objects.order_by('-pub_date')[:5],
            context_object_name='student_list',
            template_name='student/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Student,
            template_name='student/detail.html')),
    url(r'^(?P<pk>\d+)/edit/$', 'student.views.student_edit'),
    url(r'^(?P<pk>\d+)/save/$', 'student.views.student_save'),
)
