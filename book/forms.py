from django import forms
from .models import reviews

class reviewForm(forms.ModelForm):
    class Meta:
        model = reviews
        fields = ['comment']
     