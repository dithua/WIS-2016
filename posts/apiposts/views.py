from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
import json
import urllib2
from . models import Posts, Comments
from . forms import PostsForm, CommentsForm


# ------------------- Views tha get data from API------------------------------------------
def allposts(request):
	data = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts'))
	context = {'data': data}
	return render(request, 'apiposts/allposts-api.html', context)


def getpost(request, postid):
	post = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts/' + postid))
	comments = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts/' + postid + '/comments'))
	context = {'post': post, 'comments': comments, 'api': True}
	return render(request, 'apiposts/post.html', context)


def getuser(request, userid):
	user = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/users/' + userid))
	user_posts = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts?userId=' + userid))
	context = {'user': user, 'user_posts': user_posts}
	return render(request, 'apiposts/user.html', context)

# ------------------- Views tha get data from DB------------------------------------------

@login_required
def getposts_from_model(request):
	data = Posts.objects.all()
	context = {'data': data}
	return render(request, 'apiposts/allposts-db.html', context)


@login_required
def post_form(request):
	if request.method == 'GET':
		form = PostsForm()
	else:
		form = PostsForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			body = form.cleaned_data['body']
			post = Posts.objects.create(title=title, body=body, userId=request.user)
			return HttpResponseRedirect("/apiposts/dbdata/")

	return render(request, 'apiposts/newpost.html', {'form': form,})


@login_required
def get_post_by_id(request,postid):
	data = Posts.objects.get(id=postid)
	comments = Comments.objects.filter(postId=postid)
	context = {'post': data, 'comments': comments, 'api': False}
	return render(request, 'apiposts/post.html', context)


class PostListView(ListView):
	model = Posts
