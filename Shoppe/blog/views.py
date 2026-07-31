from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import Blog
def BlogMain(request):
    blogs = Blog.objects.all().order_by('created_at')
    paginator = Paginator(blogs,3)
    page_number = request.GET.get('page')
    page_obj =  paginator.get_page(page_number)
    return render(request , 'blog_main.html',{'page_obj':page_obj})
def BlogDetail(request,id):
    blog = get_object_or_404(Blog,id=id)
    next_blog = Blog.objects.filter(id__gt=blog.id).order_by('id').first()
    pre_blog = Blog.objects.filter(id__lt=blog.id).order_by('-id').first()
    return render(request, 'blog_detail.html',{'blog':blog,'next_blog':next_blog,'pre_blog':pre_blog,})