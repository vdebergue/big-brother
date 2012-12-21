from django.views.generic import DetailView, ListView
from django.conf.urls import patterns, include, url

from student.models import Student
from student.models import Company
from student.models import Internship

urlpatterns = patterns('',
    # Company urls
    url(r'^$',
        ListView.as_view(
            queryset=Internship.objects.order_by('-id')[:5],
            context_object_name='internships_list',
            template_name='company/index.html')),    
            
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Company,
            template_name='company/company.html')),
            
    url(r'^(?P<pk>\d+)/edit/$', 'company.views.company_edit'),
    url(r'^(?P<pk>\d+)/save/$', 'company.views.company_save'),

    url(r'^notified/$','student.views.notified'),
    
    #internships urls
    url(r'^internship/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Internship,
            template_name='company/internship.html')),
            
    url(r'^(?P<pk>\d+)/internship/create$', 'student.views.internship_create'),    
            
    url(r'^(?P<pk>\d+)/internship/(?P<internship_id>\d+)/edit$', 'student.views.internship_edit'),
    url(r'^(?P<pk>\d+)/internship/(?P<internship_id>\d+)/save/$', 'student.views.internship_save'),

    #students pool urls
    url(r'^(?P<pk>\d+)/pool$',
        DetailView.as_view(
            model=Company,
            template_name='company/pool.html')),
    url(r'^(?P<pk>\d+)/pool/(?P<sk>\d+)/ping/$', 'company.views.pool_ping'),     
    
)
