from django import forms
from .models import ShortNews


class NewsModelForm(forms.ModelForm):
    class Meta:
        model = ShortNews
        fields = '__all__'


class NewsForm(forms.Form):
    class Meta:
        model = ShortNews
        fields = '__all__'
