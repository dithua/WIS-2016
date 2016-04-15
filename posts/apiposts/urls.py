"""posts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^api/$', views.allposts, name='api-all' ),   # all posts from API
    url(r'^api/(?P<postid>\d+)', views.getpost, name="api-id"),   # one specific post from API
    url(r'^api/user/(?P<userid>\d+)', views.getuser, name="api-user"),  # a user's posts url from API

    url(r'^db/$', views.getposts_from_model, name="db-all"),  # all posts url from DB
    url(r'^db/(?P<postid>\d+)', views.get_post_by_id, name="db-id"),  # one specific post url from DB
    url(r'^new/$', views.post_form, name="new-post"),

    url(r'^list/$', views.PostListView.as_view(), name='posts-list'),  # list from posts from listview

]
