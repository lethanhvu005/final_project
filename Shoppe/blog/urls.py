from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.BlogMain, name='BlogMain'),
    path('<int:id>/blog_detail', views.BlogDetail, name='BlogDetail'),
    path('rate/',views.Rates, name='Rate'),
    path('comment/',views.CommentUser,name='Comment'),
    path('comment_child/',views.CommentChild,name='CommentChild'),

]
