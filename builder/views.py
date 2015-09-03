from .models import Resume, Contact
from django.contrib.auth.models import User
from builder.serializers import UserSerializer, ResumeSerializer, AboutSerializer 
from forms import ResumeForm, AboutForm, ContactForm, EducationForm, SkillForm, ExperienceForm\
,RegistrationForm

from rest_framework import generics, permissions
from rest_framework.views import APIView

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from builder.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response

from django.core.context_processors import csrf

from helper import *




def index(request):
    # renders html with list of resumes
    current_user = request.user
    resume_list = Resume.objects.filter(user=current_user)
    context = {'resumes': resume_list}
    return render(request,'builder/index.html', context)

# methods for listing, adding, editing/updating and deleting instances
#    of models including About, Contact, Education, Work and Skills

def models_index(request,resume_id,model):
    # renders Html page listing items from model matching resume_id
    # authenticate
    if not request.user == Resume.objects.get(pk=resume_id).user:
        return HttpResponseRedirect(reverse('resume_index'))
    
    model_list = get_objects_by_model(resume_id, model)
    context = {'list': model_list}
    return render(request, 'builder/model_index.html', context)

def models_add(request,resume_id, model):
    # renders empty form to add a new instance to model

    model_form = get_form_by_selection(resume_id, model,False)
    context = {'form':model_form}
    return render(request,'builder/simple_form.html', context)

def models_edit(request,resume_id, model, pk):
    # renders pre-populated form to edit existing model instance
    # applies to Education, Work and Skill Models

    if not Resume.objects.get(pk=resume_id) == get_model_object(model,pk=pk).resume_id:
        return HttpResponseRedirect(reverse('resume_index'))

    model_form = get_form_by_selection_id(pk, model)
    context = {'form':model_form, 'id': pk}

    return render(request,'builder/form_update.html', context)

def models_form_save(request, resume_id, model):
    # creates and save new model instance according to data from form
    if request.method == 'POST':
        form = get_complete_form_by_model(request.POST, model)

        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            model.resume_id = Resume.objects.get(pk=resume_id)
            model.save()
        return HttpResponseRedirect('/resume/')

    else:
        return HttpResponseRedirect('/resume/')

def models_form_update(request, model, resume_id, pk):
    # saves an existing model instance with edited data from submitted form
    if request.method == 'POST':
        form = get_updated_form_by_model(request.POST, model, pk)
        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            model.pk = pk
            model.resume_id = Resume.objects.get(pk=resume_id)
            model.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def models_form_delete(request, model, pk):
    # deletes existing model instance from database

    model = get_model_object(model, pk)

    if request.method == 'POST':
        model.delete()
    return HttpResponseRedirect(reverse('resume_index'))

### Views for Work Model ###

def work_edit(request,resume_id, pk):
    # renders editable html form populated with data from existing work instance

    if not Resume.objects.get(pk=resume_id) == Work.objects.get(pk=pk).resume_id:
        return HttpResponseRedirect(reverse('resume_index'))

    work_instance = Work.objects.get(pk=pk)
    model_form = WorkForm(instance=work_instance)
    experience_points = Experience.objects.filter(work_id=work_instance)
    context = {'form':model_form, 'experience':experience_points}

    return render(request,'builder/model_edit.html', context)

def work_save(request, resume_id, pk):
    # saves data to existing work instance using modified form data
    if request.method == 'POST':
        work_instance = (Work.objects.get(pk=pk) or None)
        form = WorkForm(request.POST,instance=work_instance)

        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            model.pk = pk
            model.resume_id = Resume.objects.get(pk=resume_id)
            model.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

### Views for Experience Model ###

def experience_edit(request,resume_id, work_id, pk):
    # renders editable html form populated with data from existing work instance

    if not Work.objects.get(pk=work_id) == Experience.objects.get(pk=pk).work_id:
        return HttpResponseRedirect(reverse('resume_index'))

    exp_instance = Experience.objects.get(pk=pk)
    form = ExperienceForm(instance=exp_instance)
    context = {'form': form}

    return render(request,'builder/model_form.html', context)

def experience_update(request, resume_id, work_id, pk):
    # saves data to existing Experience model instance using modified form data
    if request.method == 'POST':
        exp_instance = (Experience.objects.get(pk=pk) or None)
        form = ExperienceForm(request.POST,instance=exp_instance)

        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            model.pk = pk
            model.resume_id = Resume.objects.get(pk=resume_id)
            model.work_id = Work.objects.get(pk=work_id)
            model.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def experience_add(request, resume_id, work_id):
    # creates and saves new experience object using submitted form data 

    if request.method == 'POST':
        #exp_instance = (Experience.objects.get(pk=pk) or None)
        form = ExperienceForm(request.POST)

        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.resume_id = Resume.objects.get(pk=resume_id)
            experience.work_id = Work.objects.get(pk=work_id)
            experience.save()

            context = {'pk': work_id, 'resume_id': resume_id}
            args = (resume_id, work_id)
        return HttpResponseRedirect(reverse('index'))

    else: # create form to make new resume
        form = ExperienceForm(initial={'user': request.user})
        context = {}
        context.update(csrf(request))
        context['form'] = form

        return render_to_response('builder/model_add.html',context)


### Views for Resume Model ###

def create(request):
    # save entry to the resume model given data from submitted form

    if request.POST:
        instance = Resume.objects.get(request.user)
        form = ResumeForm(request.POST, instance)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('resume/about/create')
    else:
        form = ResumeForm(initial={'user': request.user})

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('builder/create_resume.html',args)

def new_resume(request):
    # renders an empty form used to create new resume instance

    if request.method == 'POST':
        # create new resume from form
        form = ResumeForm(request.POST)

        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
        return HttpResponseRedirect('/resume/')

    else: # create form to make new resume
        form = ResumeForm(initial={'user': request.user})
        args = {}
        args.update(csrf(request))
        args['form'] = form

        return render_to_response('builder/create_resume.html',args)

def edit_resume(request, pk):
    # returns editable html form for existing resume instance
    return render(request,'builder/edit_resume.html',{'pk':pk})

def delete_resume(request, pk):
    # delete existing resume instance from database
    resume = get_object_or_404(Resume, pk=pk)
    if request.method=='POST':
        resume.delete()
    return HttpResponseRedirect(reverse('resume_index'))

def update_resume(request,pk, model):
    # saves existing resume object with new data from submitted form
    model_form = get_form_by_selection(pk,str(model))
    context = {'form':model_form}

    return render(request,'builder/simple_form.html', context)

def registration_view(request):
    form = RegistrationForm(request.POST or None)
    btn = 'Join'

    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.save()
        return HttpResponseRedirect("/")

    context = {
        "form": form,
        "submit_btn": btn,
    }
    return render(request, 'builder/simple_form.html', context)

# API VIEWS

class UserDetail (generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly)

class UserList (generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly)


class ResumeList(APIView):
    
    def get(self,request, pk, format=None):
        current_user = request.user
        resume = Resume.objects.filter(user=current_user, pk=pk)
        serialized_resumes = ResumeSerializer(resume,many=True)
        return Response(serialized_resumes.data)

    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly)
    
class ContactList(APIView):
    
    def get(self,request, pk, format=None):
        current_user = request.user
        contact = Resume.objects.filter(user=current_user, pk=pk).first().contact
        serialized_contact = ContactSerializer(contact,many=True)
        return Response(serialized_contact.data)

class AboutList(APIView):
    
    def get(self,request, pk, format=None):
        current_user = request.user
        about = Resume.objects.filter(user=current_user, pk=pk).first().about
        serialized_abouts = AboutSerializer(about,many=True)
        return Response(serialized_abouts.data)
