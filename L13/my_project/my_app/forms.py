from django import forms
from .models import Task


class TaskForm(forms.Form):
    text = forms.CharField(max_length=64)
    checked = forms.BooleanField(required=False)


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'checked']
        label = {'text': 'Текст'}
        help_text = {'text': 'help text'}
