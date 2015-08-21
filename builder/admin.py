from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm

from .models import Resume, About, Contact, Education, Skill, Work, Experience
from django.contrib.auth.models import User

class ResumeInLine(admin.StackedInline):
    model = Resume
    extra = 0
    
class MyUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(MyUserChangeForm, self).__init__(*args, **kwargs)
        

class UserAdmin(admin.ModelAdmin):
    form = MyUserChangeForm
    inlines = [ResumeInLine, ]
    
class AboutInLine(admin.StackedInline):
    model = About
    extra = 0

class ContactInLine(admin.StackedInline):
    model = Contact
    extra = 0
    
class EducationInLine(admin.StackedInline):
    model = Education
    extra = 0
    

class WorkInLine(admin.StackedInline):
    model = Work
    extra = 0

class ExperienceInLine(admin.StackedInline):
    model = Experience
    extra = 0
    
class SkillsInLine(admin.StackedInline):
    model = Skill
    extra = 0

class UserInLine(admin.StackedInline):
    model = User
    extra = 0 

class ResumeAdmin(admin.ModelAdmin):
       fields = ['context']
       inlines = [AboutInLine, ContactInLine, EducationInLine,
        WorkInLine, ExperienceInLine, SkillsInLine]

# Add models to Admin App:
# Unregister default User model Admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Resume, ResumeAdmin)

