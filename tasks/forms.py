from django import forms
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from .models import User, Task


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "due_to_time", "priority"]
        widgets = {
            'due_to_time': forms.DateInput(
                attrs={
                    'type': 'date', 
                    'class': 'form-control',
                    'min': date.today().isoformat() 
                }
            ),
        }


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "due_to_time", "priority", "is_completed"]
        widgets = {
            'due_to_time': forms.DateInput(
                attrs={
                    'type': 'date', 
                    'class': 'form-control',
                    'min': date.today().isoformat() 
                }
            ),
        }