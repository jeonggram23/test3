from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        Model =Article
        exclude = ('user',)
        widgets = {
            'title':forms.TimeInput(attrs={'class': 'form-control'}),
            'content':forms.Textarea(attrs={'class': 'form-control'}),
        }
from .models import Article, Comment

class ArticleForm():
    class Meta:
        model = Article
        exclude = ('user', )



class CommentForm():
    class Meta:
        model = Comment
        fields = ('comment', )