from django import forms
from .models import Comment

class CommnentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','text']