from django import forms
from .models import Resume, About, Contact, Skill, Education, Work, Experience
from django.contrib.auth import get_user_model

User = get_user_model()


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


class RegistrationForm(forms.ModelForm):
	email = forms.EmailField(label='Your Email')
	password1 = forms.CharField(label='Password', \
					widget=forms.PasswordInput())
	password2 = forms.CharField(label='Password Confirmation', \
					widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ['username', 'email']

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords do not match")
		return password2

	def clean_email(self):
		email = self.cleaned_data.get("email")
		user_count = User.objects.filter(email=email).count()
		if user_count > 0:
			raise forms.ValidationError("This email has already been registered. Please check and try again or reset your password.")
		return email


	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1']) 
		if commit:
			user.save()
		return user