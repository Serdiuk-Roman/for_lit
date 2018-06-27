from django.contrib.auth.models import User
from django import forms



class AuthModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
