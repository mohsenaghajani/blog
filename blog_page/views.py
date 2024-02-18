from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def post(request):
    return render(request, 'blog/all-post.html')


def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')
