from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    
    url(r'^v1/resume/(?P<pk>[0-9]+)/contact', views.ContactList.as_view()),
    url(r'^v1/resume/(?P<pk>[0-9]+)/about', views.AboutList.as_view()),
    url(r'^v1/resume/(?P<pk>[0-9]+)/', views.ResumeList.as_view()),
    url(r'^v1/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^v1/(?P<username>.*)/$', views.UserList.as_view()),
	url(r'^index/$', views.index, name='resume_index'),
	url(r'^(?P<pk>[0-9]+)/edit/',views.edit_resume, name='edit_resume'),
	url(r'^([0-9]+)/(\w)/',views.update_resume, name='update_resume'),   
    url(r'^create/$', views.new_resume),
    url(r'^$', views.index, name='index'),
    
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)

