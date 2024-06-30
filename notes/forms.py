from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'name', 
            'description', 
            'deadline', 
            'priority', 
            'tags', 
            'user_tags', 
            'recipient'
        ]
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'tags': forms.CheckboxSelectMultiple,
            'user_tags': forms.CheckboxSelectMultiple,
        }