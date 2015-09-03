from rest_framework import serializers
from models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    resumes = serializers.SlugRelatedField(many=True,queryset = Resume.objects.all(),slug_field='context')
    
    class Meta(object):
        model = User
        fields = ('id','username','resumes')

class AboutSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = About
        field = {'first_name','last_name','career','about_me','photo'}

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = Contact
        field = {'email','phone_number','website','linkedin','github'}
        
class EducationSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = Education
        field = {'degree_type','program','school','city','province',
                'start_date','end_date', 'gpa'}

class SkillSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = Skill
        field = {'type','name','proficiency'}

class ExperienceSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = Experience
        field = {'description'}

class WorkSerializer(serializers.ModelSerializer):
    experience = ExperienceSerializer(many=True, read_only=False)
    
    class Meta(object):
        model = Work
        field = {'id','work_type','organization','position','city',
                'province','start_date','end_date', 'skills_used', 'experience'}

class ResumeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = False)
    about = AboutSerializer(read_only=False, many=True)
    contact = ContactSerializer(read_only=False, many=True)
    education = EducationSerializer(read_only=False, many=True)
    skill = SkillSerializer(read_only=False, many=True)
    work = WorkSerializer(read_only=False, many=True)
    
    class Meta(object):
        model = Resume
        field = {'context','user','about','contact','education','skill','work'}
        


        

    
    
