from django import forms
from .models import Note, Tag, UserTag

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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(NoteForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['user_tags'].queryset = UserTag.objects.filter(user=user)

class UserTagForm(forms.ModelForm):
    class Meta:
        model = UserTag
        fields = [
            'name',
            'description',
        ]