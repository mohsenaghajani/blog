from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def post(request):
    pass


def post_detail(request):
    pass
