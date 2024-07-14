from django import forms
from .models import blog

class blogform(forms.ModelForm):
    class Meta:
        model=blog
        fields='__all__'
