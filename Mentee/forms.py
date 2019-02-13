from django import forms
from .models import Mentee

class PostForm (forms.ModelForm):
    class Meta:
        model = Mentee
        fields = ('name', 'quotes', 'model_pic')