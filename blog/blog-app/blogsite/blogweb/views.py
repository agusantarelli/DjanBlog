from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from blogweb.models import blogPost,Author,comment
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import CreateView

def about(request):
    return render(request,'blog/about.html')

def home(request):
    queryset = request.GET.get("buscar")
    posts = blogPost.objects.all()
    if queryset:
        posts = blogPost.objects.filter(
        Q(title__icontains = queryset)
        )
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,"blog/index.html",{'posts': posts})

def postDetail(request,id):
    posts = get_object_or_404(blogPost,pk=id)
    return render(request,'blog/post.html',{'posts':posts})

def addComment(request):
    return render(request,'blog/add-comment.html')

class addPostView(CreateView):
    model = blogPost
    template_name = 'blog/add-post.html'
    fields = ('title','author','description',)

def authors(request):
    queryset = request.GET.get("buscar")
    authors = Author.objects.all()
    if queryset:
        authors = Author.objects.filter(
        Q(user__first_name__contains=queryset) |
        Q(user__last_name__contains=queryset) |
        Q(user__username__contains=queryset))
    paginator = Paginator(authors,5)
    page = request.GET.get('page')
    authors = paginator.get_page(page)
    return render(request, "blog/authors.html", {'authors': authors})
