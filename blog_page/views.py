from django.shortcuts import render
from blog_page.models import Post
# Create your views here.


def index(request):
    posts = Post.objects.order_by('create_time').all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def post(request):
    posts = Post.objects.order_by('create_time').all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/all-post.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }

    return render(request, 'blog/post-detail.html', context)
