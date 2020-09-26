from .models import  Comment, Post
from django import forms

class CommentForm(forms.ModelForm):

	class Meta:
	    model = Comment
	    fields = ['author', 'text']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']