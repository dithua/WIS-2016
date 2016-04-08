from django.forms import ModelForm
from . models import Posts,Comments


class PostsForm(ModelForm):
        class Meta:
            model = Posts
            fields = [ 'title', 'body']


class CommentsForm(ModelForm):
        class Meta:
            model = Comments
            fields = [ 'name', 'body', 'email']
