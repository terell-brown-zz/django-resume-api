from django import forms
from .models import Resume, About, Contact, Skill, Education, Work, Experience



class ResumeForm(forms.ModelForm): 

	class Meta:
		model = Resume
		fields = ['context']
		labels = {"context": "Resume Name:",}


class AboutForm(forms.ModelForm):

	class Meta:
		model = About
		exclude = ['resume_id']
		

class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		exclude = ['resume_id']

class EducationForm(forms.ModelForm):
	__name__ = 'education'
	class Meta:
		model = Education
		exclude = ['resume_id']

class SkillForm(forms.ModelForm):

	class Meta:
		model = Skill
		exclude = ['resume_id']

class WorkForm(forms.ModelForm):

	class Meta:
		model = Work
		exclude = ['resume_id']

class ExperienceForm(forms.ModelForm):

	class Meta:
		model = Experience
		exclude = ['resume_id','work_id']