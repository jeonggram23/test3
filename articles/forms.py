from django import forms
from .models import Article, Comment

class ArticleForm():
    class Meta:
        model = Article
        exclude = ('user', )



class CommentForm():
    class Meta:
        model = Comment
        fields = ('comment', )