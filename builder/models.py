from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    context = models.CharField(max_length=30)
    user = models.ForeignKey(User, related_name='resumes')
    
    def __str__(self):
        return self.context
    

class About(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    career = models.CharField(max_length=50)
    about_me = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    resume_id = models.ForeignKey(Resume,default=-1,related_name='about')
    
    def __str__(self):
        return self.first_name + self.last_name

    def getName(self):
        return self.__class__.__name__

class Contact(models.Model):
    email = models.EmailField(default="")
    phone_number = models.CharField(max_length=20,blank=True)
    website = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    resume_id = models.ForeignKey(Resume,default=-1,related_name='contact')

    def __str__(self):
        return self.email

    def getName(self):
        return self.__class__.__name__

    
class Education(models.Model):
    degree_type = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    gpa = models.IntegerField(default=-1)
    resume_id = models.ForeignKey(Resume,default=-1,related_name='education')

    def __str__(self):
        return self.program + " @ " + self.school 

    def getName(self):
        return self.__class__.__name__
    
class Skill(models.Model):
    name = models.CharField(max_length = 30)
    skill_type = models.CharField(max_length=30)
    proficiency = models.IntegerField(default=0)
    resume_id = models.ForeignKey(Resume,default=-1,related_name='skill')

    def __str__(self):
        return self.name

    def getName(self):
        return self.__class__.__name__

class Work(models.Model):
    work_type = models.CharField(max_length=30)
    organization = models.CharField(max_length=50)
    position = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    skills_used = models.TextField()
    resume_id = models.ForeignKey(Resume,default=-1,related_name='work')
    
    def __str__(self):
        return self.position + " @ " + self.organization

    def getName(self):
        return str(self.__class__.__name__)

class Experience(models.Model):
    description = models.TextField()
    work_id = models.ForeignKey(Work,related_name='experience')
    resume_id = models.ForeignKey(Resume,default=-1)

    def __str__(self):
        return self.description + " @ " + self.work_id.organization

    def getName(self):
        return self.__class__.__name__    
    


