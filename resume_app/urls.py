"""resume_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('builder.urls')),
    url(r'^home/', include('builder.urls')),

    # accessing experience model data:

    url(r'^resume/(?P<resume_id>[0-9]+)/edit/work/(?P<work_id>[0-9]+)/add/experience/', 'builder.views.experience_add'),
    url(r'^resume/(?P<resume_id>[0-9]+)/edit/work/(?P<pk>[0-9]+)/save/', 'builder.views.work_save'),
    url(r'^resume/(?P<resume_id>[0-9]+)/edit/work/(?P<work_id>[0-9]+)/experience/(?P<pk>[0-9]+)/edit/update/', 'builder.views.experience_update'),
    url(r'^resume/[0-9]+/edit/work/([0-9]+)/(?P<model>.*)/(?P<pk>[0-9]+)/delete/', 'builder.views.models_form_delete'),
    url(r'^resume/(?P<resume_id>[0-9]+)/edit/work/(?P<work_id>[0-9]+)/experience/(?P<pk>[0-9]+)/edit/', 'builder.views.experience_edit'),
    

    # acessing resume model data:
    url(r'^resume/save', 'builder.views.new_resume',name='new_resume'),
    url(r'^resume/(?P<pk>[0-9]+)/delete/', 'builder.views.delete_resume',name='delete_resume'),

    # edit models with multiple instances per user:
    url(r'^resume/(?P<resume_id>[0-9]+)/edit/(?P<model>.*)/(?P<pk>[0-9]+)/update/', 'builder.views.models_form_update',name='models_form_update'),
    url(r'^resume/([0-9]+)/edit/(?P<model>.*)/(?P<pk>[0-9]+)/delete/', 'builder.views.models_form_delete',name='models_form_delete'),
    url(r'^resume/(?P<resume_id>[0-9]+)/edit/(?P<model>.*)/save', 'builder.views.models_form_save',name='models_form_save'),
    url(r'^resume/(?P<resume_id>[0-9]+)/edit/work/(?P<pk>[0-9]+)/', 'builder.views.work_edit', name='work_edit'),
    url(r'^resume/(?P<resume_id>[0-9]+)/edit/(?P<model>.*)/(?P<pk>[0-9]+)', 'builder.views.models_edit'),
    url(r'^resume/(?P<resume_id>[0-9]+)/edit/(?P<model>.*)/add', 'builder.views.models_add'),
    url(r'^resume/(?P<resume_id>[0-9]+)/edit/(?P<model>.*)/', 'builder.views.models_index'),
    url(r'^resume/(?P<pk>[0-9]+)/edit/(?P<model>.*)/', 'builder.views.update_resume'),
    url(r'^resume/', include('builder.urls')),

    url(r'^api/user/', include('builder.urls')),   
    url(r'^api/', include('builder.urls')),

    # authentication
    url(r'^login/$','django.contrib.auth.views.login',{'template_name':'./auth/login.html'},name='password_reset'),
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page': '/'}),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^register/', 'builder.views.registration_view', name='registration'),  
    url(r'^$', 'django.contrib.auth.views.login',{'template_name':'auth/login.html'},name='password_reset'),    
    url(r'^rest-auth/', include('rest_auth.urls')),
]

# if settings.DEBUG:
#     urlpatterns =+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns =+ static(settings.MEDIA_URL, document_root=settings.STATIC_MEDIA)