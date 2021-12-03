# students/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from courses.models import Course

class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(),
                                    widget=forms.HiddenInput)
    
    
class InstructorRegistrationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', )