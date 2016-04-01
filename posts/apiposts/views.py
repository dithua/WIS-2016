from django.shortcuts import render
import json
import urllib2

# Create your views here.


def allposts(request):
	data = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts'))
	context = {'data': data}
	return render(request, 'apiposts/allposts.html', context)


def getpost(request, postid):
	post = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts/'+postid))
	comments = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts/'+postid+'/comments'))
	context = {'post': post, 'comments': comments}
	return render(request, 'apiposts/post.html', context)


def getuser(request, userid):
	user = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/users/'+userid))
	user_posts = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts?userId='+userid))
	context = {'user': user, 'user_posts': user_posts}
	return render(request, 'apiposts/user.html', context)
