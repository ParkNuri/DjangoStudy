from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.forms import inlineformset_factory
from django.db.models import Count
from django.contrib.auth.decorators import login_required
# POST방식이 아닌 방식으로 삭제 감지 시 에러 발생
from django.views.decorators.http import require_POST
# Create your views here.
def index(request):
#    articles = Article.objects.all()
    articles = Article.objects.values().annotate(comment_cnt=Count('comment'))
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    # 1은 N을 보장할 수 없기 때문에 querySet(comment_set)형태로 조회해야한다.
    comments = article.comment_set.all()
    comments_cnt = article.comment_set.count()
    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments,
        'comments_cnt' : comments_cnt
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def create_comment(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
    #comment = Comment()
        
    # if request.method == "POST":
    #     comment.content = request.POST.get('content')
    #     comment.article_id = article_pk
    #     comment.save()
        # form = CommentForm(request.POST)
    # if request.method == "POST" :
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()        
            return redirect('articles:detail', article_pk)
        else:
            context = {
                'comment_form' : comment_form,
                'article' : article
            }
            return render(request, 'articles/index.html', context)
    else :
        return redirect('accounts:login')

@require_POST
def delete_comment(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
    # article_pk = comment.article_id
        # if request.method == "POST":
        if comment.user == request.user:
            comment.delete()
        return redirect('articles:detail', article_pk)
    else:
        return redirect('account:login')
    
@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, '게시글 작성 완료!!!!!')
            return redirect('articles:detail', article.pk)
        else:
            messages.error(request, '잘못된 데이터를 입력하였습니다.')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.user == request.user:
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILE, instance=article)
            if form.is_valid():
                article = form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'form': form
        }
        return render(request, 'articles/form.html', context)
    else:
        return redirect('articles:detail', article.pk)

@require_POST
@login_required
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        # if request.method == "POST":
        if article.user == request.user:
            article.delete()
            return redirect('articles:index')
        else:
            return redirect('articles:detail', article.pk)
    return redirect('articles:login')


