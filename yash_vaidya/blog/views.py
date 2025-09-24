from django.shortcuts import render, get_object_or_404, redirect  # this all for update, create the post
from django.contrib.auth.decorators import login_required # this is also for create but also for login.
from .models import blog_post
from .forms import blogpost_form

# Create your views here.
def home (request):
    return render(request, 'iindex.html')

@login_required
def post_create(request):
    if request.method == "POST":
        form = blogpost_form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit= False) # don't save it to Database yet
            post.author = request.user # set current user as author
            post.save()  # now save it to database
            return redirect('post_list')  
    else:
        form = blogpost_form()

    return render(request, "blog/post_create.html", {'form' : form})
    
    
    

def post_list(request):
    posts = blog_post.objects.all().order_by('-created_at')
    return render(request, "blog/post_list.html", {'posts': posts})




def post_details(request, post_id):
    post = get_object_or_404(blog_post, id = post_id)
    return render(request, "blog/post_details.html", {'post' : post})


@login_required
def post_update(request, post_id):

    # Fatching the post that matches to the ID and belongs to the current user
    post = get_object_or_404(blog_post, pk = post_id, author = request.user)

    if post.author != request.user:
        return redirect('post_list') # user is not the author, redirect

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
        return redirect('post_list')  # user is not the author, redirect

    if request.method == "POST":
        post.delete()
        return redirect("post_list")
    
    return render(request, "blog/post_delete.html", {'post': post})




    

