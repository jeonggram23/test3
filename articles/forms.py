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