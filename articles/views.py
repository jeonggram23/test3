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