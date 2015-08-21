from builder.models import *
from builder.forms import AboutForm, ContactForm, EducationForm, WorkForm, SkillForm
from builder.serializers import UserSerializer, ResumeSerializer, AboutSerializer, ContactSerializer, EducationSerializer, ExperienceSerializer
from django.forms.formsets import formset_factory
from django.shortcuts import get_object_or_404


# helper functions used throughout the project


def get_form_by_selection(resume_id, model, populate=True):
	# returns an empty form object according to model string provided
	# if populte=True the form is populated before being return

	if populate:
		instance = get_model_instance(resume_id,model)
	else: 
		instance = None

	return get_form(model, instance)

def get_form(model, instance):
	# returns a form based on model type and instance of model provided
	
	if model == 'about':
		return AboutForm(instance=instance)
	elif model == 'contact':
		return ContactForm(instance=instance)
	elif model == 'education':
		return EducationForm(instance=instance)
	elif model == 'work':
		return WorkForm(instance=instance)
	elif model == 'skill':
		return SkillForm(instance=instance)


def get_form_by_selection_id(model_id, model):
	# returns populated form depending on the model and model_id provided

	instance = get_model_object(model, model_id)
	return get_form(model, instance)

def get_objects_by_model(resume_id, model):
	# returns array of objects matching resume_id for model provided

	if model == 'about':
		return About.objects.filter(resume_id=resume_id)
	elif model == 'contact':
		return Contact.objects.filter(resume_id=resume_id)
	elif model == 'education':
		return Education.objects.filter(resume_id=resume_id)
	elif model == 'work':
		return Work.objects.filter(resume_id=resume_id)
	elif model == 'skill':
		return Skill.objects.filter(resume_id=resume_id)
	else:
		return None

def get_complete_form_by_model(form_data, model):
	# returns a form according to model provided, populated
	#   with data from URL request

	if model == 'about':
		return AboutForm(form_data)
	elif model == 'contact':
		return ContactForm(form_data)
	elif model == 'education':
		return EducationForm(form_data)
	elif model == 'work':
		return WorkForm(form_data)
	elif model == 'skill':
		return SkillForm(form_data)
	else:
		return None

def get_updated_form_by_model(form_data, model, pk):
	# returns model form with data from existing model object (given by pk) 
	# but overridden by form data
	if model == 'about':
		return AboutForm(form_data, instance=About.objects.get(pk=pk))
	elif model == 'contact':
		return ContactForm(form_data, instance=Contact.objects.get(pk=pk))
	elif model == 'education':
		return EducationForm(form_data,instance=Education.objects.get(pk=pk))
	elif model == 'work':
		return WorkForm(form_data,instance=Work.objects.get(pk=pk))
	elif model == 'skill':
		return SkillForm(form_data, instance=Skill.objects.get(pk=pk))
	else:
		return None

def get_model_object(model, pk):
	# returns existing model object according to model type and 
	#   primary key, pk. Returns 404 response if non existent

	if model == 'about':
		return get_object_or_404(About, pk=pk)
	elif model == 'contact':
		return get_object_or_404(Contact, pk=pk)
	elif model == 'education':
		return get_object_or_404(Education, pk=pk)
	elif model == 'work':
		return get_object_or_404(Work, pk=pk)
	elif model == 'skill':
		return get_object_or_404(Skill, pk=pk)
	elif model == 'experience':
		return get_object_or_404(Experience, pk=pk)
	else:
		return None

def get_serialized_model(request, model, resume_id):
	
	if model == 'about':
		model_instance = About.objects.filter(resume_id=resume_idk)
		return AboutSerializer(About, many=True)
	elif model == 'contact':
		model_instance = Contact.objects.filter(resume_id=resume_id)
		return ContactSerializer(Contact, many=True)
	elif model == 'education':
		model_instance = Education.objects.filter(resume_id=resume_id)
		return EducationSerializer(Education, many=True)
	elif model == 'work':
		model_instance = Work.objects.filter(resume_id=resume_id)
		return WorkSerializer(Work, many=True)
	elif model == 'skill':
		model_instance = Skill.objects.filter(resume_id=resume_id)
		return SkillSerializer(Skill, many=True)
	elif model == 'experience':
		model_instance = Experience.objects.filter(resume_id=resume_id)
		return ExperienceSerializer(Experience, many=True)
	else:
		return None






	