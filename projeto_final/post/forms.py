from dataclasses import field
from django import forms
from .models import Postagem

class PostForm(forms.ModelForm):

    class Meta:
        model = Postagem
        fields = ("__all__")