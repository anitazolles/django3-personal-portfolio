from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    #blog_count=Blogs.objects.count
    blogs = Blog.objects.order_by('-date')#[:5] ## order by date ## [:5] the upper five so the five most recent ones
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) #primary key is pk
    return render(request, 'blog/detail.html',{'blog':blog})
