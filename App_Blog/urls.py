from django.urls import path
from App_Blog import views

app_name="App_Blog"

urlpatterns = [
    path('', views.BlogHome.as_view(), name='index'),
    path('write_blog/', views.WriteBlog.as_view(), name='write_blog'),
    path('details/<str:slug>/', views.blog_details, name='details'),
    path('liked/<pk>/', views.liked, name='liked'),
    path('unliked/<pk>/', views.unliked, name='unliked'),
    path('my_blogs/', views.Show_My_Blog.as_view(), name='my_blogs'),
    path('update_blog/<pk>/', views.UpdateBlog.as_view(), name='update_blog'),
    path('delete_blog/<pk>/', views.DeleteBlog.as_view(), name='delete_blog'),
]
