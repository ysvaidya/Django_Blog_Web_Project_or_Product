from django import forms 
from .models import blog_post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class blogpost_form(forms.ModelForm):

    class Meta :
        model = blog_post
        fields = ['title', 'body']
        widgets = {
            "title": forms.TextInput(attrs={
                'placeholder': "What's your story title...",
                'required': True,
                'class': 'outline-none w-full border p-2 rounded-xl border-gray-300 focus:border-gray-400 hover:bg-gray-100 focus:bg-gray-100 text-gray-400 focus:text-gray-800',
            }),

            "body": forms.Textarea(attrs={
                'id': 'content',
                'rows':10,
                'cols':30,
                'required': True,
                'placeholder':"what's your story title...",
                'class':"outline-none w-full border p-2 rounded-xl border-gray-300 focus:border-gray-400 hover:bg-gray-100 focus:bg-gray-100 text-gray-400 focus:text-gray-800",
                
            }),
        }

class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        widget={
        }
