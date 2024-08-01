from django.shortcuts import render, redirect
from .models import Post
from .forms import BlogPostForm
from django.contrib import messages

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,"index.html",{"posts":posts})
def post(request,pk):
    posts = Post.objects.get(id=pk)
    return render(request,"posts.html",{"posts":posts})
def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"your post has been crated successfully")
            return redirect("index")
        else:
            messages.error(request, 'There was an error with your form. Please correct the errors below.')
    else:
        form = BlogPostForm()

    return render(request,"create_post.html")