from django import forms 
from .models import blog_post

class blogpost_form(forms.ModelForm):
    class Meta :
        model = blog_post
        fields = ['title', 'slug', 'body']