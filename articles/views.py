<<<<<<< HEAD
from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article




# Create your views here.
def index(request):
    
    articles = Article.objects.all()
    form = CommentForm()
    
    context = {
        'articles': articles,
        'form': form,
    }
    
    return render(request, 'index.html', context)

def create(request):
    pass
def comment_create(request):
    pass
=======
from django.shortcuts import render
from .models import Article
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles' : articles
    }
    return render(request, 'index.html', context)
>>>>>>> d7ec2c25f06fb9af9bc4e744f0a9afd969b6e0db
