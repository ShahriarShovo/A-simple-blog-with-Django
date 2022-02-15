from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    author=models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)
    blog_title=models.CharField(max_length=264,verbose_name='Blog Title')
    slug=models.SlugField(max_length=264,unique=True)
    blog_content=models.TextField(verbose_name='whats in your Mide')
    blog_image=models.ImageField(upload_to='Blog_Images',verbose_name='Image')
    blog_publish_date=models.DateTimeField(auto_now_add=True)
    blog_update_date=models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    user=models.ForeignKey(User,related_name='user_comment',on_delete=models.CASCADE)
    comment=models.TextField()
    comment_date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment

class Likes(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='liked_blog')
    user=models.ForeignKey(User,related_name='liker_user',on_delete=models.CASCADE)




