from itertools import count

from django.db.models.aggregates import Avg
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Blog,Rate,Comment
def BlogMain(request):
    blogs = Blog.objects.all().order_by('created_at')
    paginator = Paginator(blogs,3)
    page_number = request.GET.get('page')
    page_obj =  paginator.get_page(page_number)
    for blog in page_obj:
        rate_avg =Rate.objects.filter(blog=blog).aggregate(avg=Avg('rate'))['avg'] or 0
        blog.rate_avg = rate_avg or 0
    return render(request , 'blog_main.html',{'page_obj':page_obj})
def BlogDetail(request,id):
    blog = get_object_or_404(Blog,id=id)
    next_blog = Blog.objects.filter(id__gt=blog.id).order_by('id').first()
    pre_blog = Blog.objects.filter(id__lt=blog.id).order_by('-id').first()
    blog_comments = Comment.objects.filter(blog_id=id,level=0).order_by('time')
    for comment in blog_comments:
        comment.child =Comment.objects.filter(blog_id=id,level=comment.id).order_by('time')
    count_comment = Comment.objects.filter(blog_id=id).count()
    return render(request, 'blog_detail.html',{'blog':blog,'next_blog':next_blog,'pre_blog':pre_blog,'blog_comments':blog_comments,'count_comment':count_comment,})
@csrf_exempt
def Rates(request):
    if request.method == 'POST':
        rate = request.POST.get('rate')
        id_blog = request.POST.get('id_blog')
        id_user = request.user
        try:
            blog = Blog.objects.get(id= id_blog)
            if Rate.objects.filter(blog=blog,user=id_user):
                rate_avg = Rate.objects.filter(blog=blog).aggregate(avg=Avg('rate'))["avg"] or 0
                return JsonResponse({'success':False,'err':'Bạn đã đánh giá rồi','rate_avg':rate_avg})
            rate_avg = Rate.objects.filter(blog=blog).aggregate(avg=Avg('rate'))["avg"] or 0
            Rate.objects.create(rate=rate,blog=blog,user=id_user)
            return JsonResponse({'success':True,'rate_avg':rate_avg})
        except Blog.DoesNotExist:
            return JsonResponse({'success':False,'err':'Blog Not Found'})
    return JsonResponse({'success':False,'err':'K thấy request nào'})
def CommentUser(request):
    if request.method == 'POST':
        cmt = request.POST.get('cmt')
        id_blog = request.POST.get('id_blog')
        user = request.user
        username= request.user.username
        avatar = request.user.avatar
        try:
            blog = Blog.objects.get(id=id_blog)
            comment=Comment.objects.create(cmt=cmt,blog=blog,user=user,name_user=username,avatar=avatar)
            return JsonResponse({'success':True,
                                'id':comment.id,
                                'cmt':comment.cmt,
                                'username':comment.name_user,
                                'avatar':str(comment.avatar),
                                'time':comment.time.strftime('%H:%M'),
                                'date':comment.time.strftime('%D/%M/%Y')})
                                
        except Blog.DoesNotExist:
            return JsonResponse({'success':False,'err': 'Blog không tồn tại'})
def CommentChild(request):
    if request.method == 'POST':
        cmt = request.POST.get('cmt')
        id_blog = request.POST.get('id_blog')
        id_cmt =request.POST.get('id_cmt')
        user = request.user
        username= request.user.username
        avatar = request.user.avatar
        try:
            blog = Blog.objects.get(id=id_blog)
            comment=Comment.objects.create(cmt=cmt,blog=blog,user=user,name_user=username,avatar=avatar,level=id_cmt)
            return JsonResponse({'success':True,
                                            'id':comment.id,
                                            'cmt':comment.cmt,
                                            'username':comment.name_user,
                                            'avatar':str(comment.avatar),
                                            'time':comment.time.strftime('%H:%M'),
                                            'date':comment.time.strftime('%D/%M/%Y')})
        except Blog.DoesNotExist:
            return JsonResponse({'success':False,'err': 'Blog không tồn tại'})