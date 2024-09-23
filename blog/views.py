from django.shortcuts import render
from .models import Post
import os
from django.conf import settings

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def post(request, post_id):
    posts = Post.objects.get(id=post_id)
    return render(request, 'post.html', {'posts': posts})