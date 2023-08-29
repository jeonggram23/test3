from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article
from django.shortcuts import render




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

# Create your views here.
def index(request):
    return render()