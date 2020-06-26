from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):# 전체 데이터 가져오기
    articles = Article.objects.all()[::-1]
    # 그 데이터 템플릿에게 넘겨주기
    context = {
        'articles': articles
    }
    # 템플릿에서 반복문으로 각각의 게시글의
    # pk, title 보여주기
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')

#def create(request):
#    title = request.GET.get('title')
#    content = request.GET.get('content')
#    context = {
#        'title':title,
#        'content':content 
#    }

#    return render(request, 'articles/create.html', context)

def introduce(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    return render(request, 'articles/introduce.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 데이터 생성을 위한 ORM 활용
    # 첫번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # aritcle.save()

    # 두번째 방법
    #article = Article(title=title, content=content)
    #article.save()

    Article.objects.create(title=title, content=content)
    # 어떤 방식을 사용 했는가에 따라서
    # save() 메서드를 사용 할 것인지 아닌지 
    return redirect('articles:index')

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html',context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article_pk)

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context={
        'article':article,
    }
    return render(request, 'articles/edit.html', context)    

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    title = request.POST.get('title')
    content = request.POST.get('content')
    article.title = title
    article.content = content
    article.save()
#    article.update(title=title, content=content)
    return redirect('articles:detail', article.pk)