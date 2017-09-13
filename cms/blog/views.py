from django.shortcuts import render
from blog.models import Post
# Create your views here.

def list_of_post(request):
	post = Post.objects.all()
	template = 'blog/post/list_of_post.html'
	context= {'post': post}
	return render(request, template, context)