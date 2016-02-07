from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Post
# Create your views here.

def home(request):
	if request.method == 'GET':
		return render(request, 'add_post.html')
	else:
		post = publish(request)
		posts = grab_all_post()
		context = dict()
		context['posts'] = posts
		return render(request, 'posts.html', context)

def publish(request):
	post = Post()
	post.author = User.objects.get(id=request.POST['author'])
	post.title = request.POST['title']
	post.text = request.POST['text']
	post.created_date = request.POST['created_date']
	post.published_date = request.POST['published_date']
	post.save()

def posts(request):
	posts = grab_all_post()
	context = dict()
	context['posts'] = posts
	return render(request, 'posts.html', context)

def grab_all_post():
	posts = Post.objects.all()
	return posts

def post_link(request, post_id):
	print post_id,"\n\n\n"
	post = Post.objects.get(id=post_id)
	context = dict()
	context['post'] = post
	return render(request, 'post.html', context)