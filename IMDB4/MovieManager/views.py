
from .models import Movie


from django.shortcuts import render
from django.http import HttpResponse





def show_details_movie(request, name):
    movie = Movie.objects.get(name=name)
    director = movie.get_directors()
    writer = movie.get_writers()
    genre=movie.genre.all()[0].name
    count_critic_criticism = movie.get_critic_criticism_count()
    count_user_criticism = movie.get_user_criticism_count()
    movie_images = movie.get_movie_images()
    main_actors = movie.mainCharacters.all()
    actors = movie.get_actors()
    context = {'movie':movie, "director":director, "writer":writer, "count_critic_criticism":count_critic_criticism,
               "count_user_criticism":count_user_criticism,"genre": genre, "movie_images":movie_images, "main_actors":main_actors,
               "actors":actors}
    return render(request, "MovieManager/movie.html", context)





def top_100_movies(request):
    movies = Movie.objects.order_by('rate')
    context = {'Movies': movies,}
    return render(request, 'top100.html', context)