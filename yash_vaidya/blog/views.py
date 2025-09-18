from django.shortcuts import render
from .models import blog_post
from .forms import blogpost_form

# Create your views here.
def home (request):
    return render(request, 'iindex.html')

