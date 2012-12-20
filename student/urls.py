from django.views.generic import DetailView, ListView
from django.conf.urls import patterns, include, url

from student.models import Student


urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Student.objects.order_by('-pub_date')[:5],
            context_object_name='student_list',
            template_name='student/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Student,
            template_name='student/detail.html')),
    url(r'^company/(?P<pk>\d+)\$',
    model=Company.as_view(
    model=Company,
    template_name='company/company.html')),

    url(r'^company/stage(?P<pk>\d+)\$',
    model=Internship.as_view(
    model=Internship,
    template_name='company/internship.html')),
)
