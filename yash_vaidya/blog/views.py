from django.shortcuts import render, get_object_or_404, redirect  # this all for update, create the post
from django.contrib.auth.decorators import login_required # this is also for create but also for login.
from .models import blog_post
from .forms import blogpost_form, UserRegistrationForm
from django.contrib.auth import login, logout
import markdown
from django.utils.safestring import mark_safe
from django.contrib import messages

def about(request):
    return render(request, 'about.html')

# Create your views here.
def home(request):
    posts = blog_post.objects.filter(status="published").order_by('-created_at')
    return render(request, "iindex.html", {'posts': posts})

def user_post(request):
    posts = blog_post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'about_Sec/my_blog.html', {'posts': posts})

@login_required
def post_create(request):
    if request.method == "POST":
        form = blogpost_form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit= False) # don't save it to Database yet
            post.author = request.user # set current user as author

            action = request.POST.get('action')
            print("ACTION:", action)

            if action == 'draft':
                post.status = 'draft'
            else:
                post.status = 'published'

            post.save()  # now save it to database
            return redirect('home')  
    else:
        form = blogpost_form()

    return render(request, "blog/post_create.html", {'form' : form})

@login_required
def draft_posts(request):
    drafts = blog_post.objects.filter(author=request.user, status='draft').order_by('-created_at')
    return render(request, 'about_Sec/draft_post.html', {'drafts': drafts})
    

def post_details(request, post_id):
    post = get_object_or_404(blog_post, id = post_id)
    post.body = markdown.markdown(post.body, extensions=['fenced_code',  # for code blocks
            'tables',       # for tables
            'nl2br',        # for line breaks
            'sane_lists',
            ])
    
    return render(request, "blog/post_details.html", {'post' : post})


@login_required
def post_update(request, post_id):

    # Fatching the post that matches to the ID and belongs to the current user
    post = get_object_or_404(blog_post, pk = post_id, author = request.user)

    if post.author != request.user:
        return redirect('home') # user is not the author, redirect

    # If form is gatting submmitted
    if request.method == "POST":

        # Bind form with submitted data + files, tied to the existing post
        form = blogpost_form(request.POST, request.FILES, instance = post) 
        if form.is_valid():  # Chacking the data is correct
            form.save()  # update the post in database
            return redirect("post_details", post_id = post.id) # going back to post_details page
    else:
        # 3. If it's a GET request, show the form with existing post data
        form = blogpost_form(instance=post)

    return render(request,'blog/post_update.html', {'form': form})
    
    
@login_required
def post_delete(request, post_id):

    post = get_object_or_404(blog_post, pk = post_id, author = request.user)

    if post.author != request.user:
        return redirect('home')  # user is not the author, redirect

    if request.method == "POST":
        post.delete()
        return redirect("home")
    
    return render(request, "blog/post_delete.html", {'post': post})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect("home")
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form' : form})

def logout_view(request):
    logout(request)
    return redirect('login')

    

