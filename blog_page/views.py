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
    return render(request, 'blog/all-post.html')


def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')
