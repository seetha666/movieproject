from django.shortcuts import render
from testapp.models import Movie
from testapp.forms import MovieForm
# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')

def list_movie(request):
    list_movies=Movie.objects.all()
    return render(request,'testapp/list_movies.html',{'list_movies':list_movies})

def add_movie_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index_view(request)
    return render(request,'testapp/addmovie.html',{'form':form})
