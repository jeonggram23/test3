from django import forms
from .models import Article, Comment

<<<<<<< HEAD
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        
        exclude = ('user', )
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        
        fields = ('content', )
=======
class ArticleForm():
    class Meta:
        model = Article
        exclude = ('user', )



class CommentForm():
    class Meta:
        model = Comment
        fields = ('comment', )
>>>>>>> d7ec2c25f06fb9af9bc4e744f0a9afd969b6e0db
