from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method=="POST":
        form = ArticleForm(request.POST)
        # 유효 true, x false
        if form.is_valid():
            # article = Article.objects.get()
            # form에 담긴 정보가 ArticleForm 
            # ArticleForm은 Article의 정보를 
            article = form.save()
            return redirect('articles:index')
    else:   # GET method 호출 시
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/form.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form
    }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    print(dir(request.resolver_match.url_name))
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)