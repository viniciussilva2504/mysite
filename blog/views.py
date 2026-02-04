from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from blog.models import Post


def home(request):
    return HttpResponse("hello world!")


class PostView(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_list'
    queryset = Post.objects.filter(status=1).order_by('-created_on')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'    