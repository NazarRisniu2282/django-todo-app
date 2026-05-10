from django import forms
from datetime import date
from tasks.models import Room, RoomTask


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["name", "description", "password"]


class RoomTaskForm(forms.ModelForm):
    class Meta:
        model = RoomTask
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


class RoomTaskUpdateForm(forms.ModelForm):
    class Meta:
        model = RoomTask
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


class RoomPasword(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="Введіть пароль від кімнати")