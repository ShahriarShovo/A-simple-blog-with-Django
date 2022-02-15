from pyexpat import model
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView
import uuid
from App_Blog.models import Blog,Likes,Comment
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from App_Blog.forms import CommentForm
# Create your views here.


class Show_My_Blog(LoginRequiredMixin,TemplateView):
    template_name='App_Blog/my_blogs.html'


class WriteBlog(LoginRequiredMixin,CreateView):
    template_name='App_Blog/write_blog.html'
    model=Blog
    fields=('blog_title','blog_content', 'blog_image')
    
    def form_valid(self, form):
        blog_object=form.save(commit=False)
        blog_object.author=self.request.user
        title=blog_object.blog_title
        blog_object.slug=title.replace(" ", "-") +"-"+str(uuid.uuid4())
        blog_object.save()
        return HttpResponseRedirect(reverse('App_Blog:index'))


class BlogHome(ListView):
    context_object_name='blogs'
    model=Blog
    template_name='App_blog/blog_list.html'





@login_required
def blog_details(request, slug):
    blog= Blog.objects.get(slug=slug)
    user_comment=CommentForm()
    already_liked=Likes.objects.filter(blog=blog, user=request.user)
    if already_liked:
        liked=True
    else:
        liked=False
    if request.method== 'POST':
        user_comment=CommentForm(request.POST)
        if user_comment.is_valid():
            comment=user_comment.save(commit=False)
            comment.user=request.user
            comment.blog=blog
            comment.save()
            return HttpResponseRedirect(reverse('App_Blog:details', kwargs={'slug':slug}))

    return render(request,'App_Blog/blog_details.html', context={'blog':blog, 'user_comment':user_comment, 'liked':liked})

@login_required
def liked(request,pk):
    blog=Blog.objects.get(pk=pk)
    user=request.user
    already_liked=Likes.objects.filter(blog=blog, user=user)
    if not already_liked:
        liked_post=Likes(blog=blog, user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('App_Blog:details', kwargs={'slug':blog.slug}))

@login_required
def unliked(request,pk):
    blog=Blog.objects.get(pk=pk)
    user=request.user
    already_liked=Likes.objects.filter(blog=blog, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Blog:details', kwargs={'slug':blog.slug}))

class UpdateBlog(LoginRequiredMixin,UpdateView):
    model= Blog
    fields=('blog_title','blog_content','blog_image')
    template_name='App_Blog/update_blog.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Blog:details', kwargs={'slug':self.object.slug})

class DeleteBlog(LoginRequiredMixin, DeleteView):
    model=Blog
    context_object_name='delete_blog'
    template_name='App_Blog/delete.html'

    def get_success_url(self) :
        return reverse_lazy('App_Blog:my_blogs')
