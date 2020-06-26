from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm
# Create your views here.
def list(request):
    movies = Movie.objects.all()
    
    context = {
        'movies' : movies
    }
    return render(request,'movies/list.html', context)

def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)

        if form.is_valid():
            movie = form.save()   
            return redirect('movies:list')

    else:
        form = MovieForm()
        context = {
            'form' : form
        }
    return render(request, 'movies/form.html', context)


def detail(request, movie_pk):

    movie = get_object_or_404(Movie, pk = movie_pk)
    #movie = Movie.objects.get(pk = movie_pk)
    
    context = {
        'movie' : movie
    }

    return render(request, 'movies/detail.html', context)

def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    # 수정버튼 클릭시 => DB수정 => detail 페이지
    if request.method == "POST":   
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
        return redirect('movies:detail', movie_pk)
    # 수정 페이지 접근시 -> 수정페이지 보여주기
    else:
        form = MovieForm(instance=movie)
        context = {
            'form' : form
        }
    return render(request, 'movies/form.html', context)

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('movies:list')
