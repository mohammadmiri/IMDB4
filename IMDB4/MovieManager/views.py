
from .models import Movie, Award, Avamel, Reviewer_Review, User_Review, Post, Movie_Celebrity_Image
from CelebrityManager.models import Celebrity

from django.shortcuts import render
from django.http import HttpResponse




# this function render the main page of each movie and show its detail (e.g. actors, director, ...)
def show_movie(request, id):
    print('before all'+id)
    movie = list(Movie.objects.filter(id=id))[0]
    print('after getting movie')
    reviewer_review_count = Reviewer_Review.objects.filter(movie=movie, show_it=True).count()
    user_review_count = User_Review.objects.filter(movie=movie, show_it=True).count()
    award_simorgh_count = Award.objects.filter(movie=movie, festival=0, candidate_type=0 ).count()
    award_cinemaHome_count = Award.objects.filter(movie=movie, festival=1, candidate_type=0).count()
    candidate_simorgh_count = Award.objects.filter(movie=movie, festival=0, candidate_type=1).count()
    candidate_cinemaHome_count = Award.objects.filter(movie=movie, festival=1, candidate_type=1).count()
    total_candidate_count = candidate_cinemaHome_count+candidate_simorgh_count
    total_award_count = award_cinemaHome_count+award_simorgh_count
    images = movie.images.all()[:4]
    actors = movie.get_actors()
    # avamel
    kargardan = list(Celebrity.objects.filter(agent__movie=movie, agent__role='kargardan'))
    nevisande = list(Celebrity.objects.filter(agent__movie=movie, agent__role='nevisande'))
    # review
    user_review = list(User_Review.objects.filter(movie=movie, show_it=True).order_by('date'))
    posts = list(Post.objects.filter(movie=movie, show_it=True).order_by('date')[:50])

    # test
    for person in kargardan:
        print('person: '+person.name)
    for image in images:
        print('image: '+image.image.url)

    context = {'movie':movie, 'reviewer_review_count':reviewer_review_count, 'user_review_count':user_review_count,
               'award_simorgh_count':award_simorgh_count, 'total_award_count':total_award_count
                ,'total_candidate_count':total_candidate_count, 'actors':actors, 'images':images,'kargardan':kargardan, 'nevisande':nevisande,
               'user_review':user_review, 'posts':posts,}
    return render(request, 'MovieManager/movie2.html', context=context)






# this function is used to serve top 100 movie page the site
def top_100_movies(request):
    movies = Movie.objects.order_by('rate')[:100]
    context = {'Movies': movies,}
    return render(request, 'top100.html', context)




def show_award_movie(request, movie_name):
    movie = Movie.objects.get(name=movie_name)
    simorgh_awarded = list(Award.objects.filter(movie=movie, festival=0, candidate_type=0))
    simorgh_candidate = list(Award.objects.filter(movie=movie, festival=0, candidate_type=1))
    simorgh_diploma = list(Award.objects.filter(movie=movie, festival=0, candidate_type=2 ))
    cinemaHome_awarded = list(Award.objects.filter(movie=movie, festival=1, candidate_type=0))
    cinemaHome_candidate = list(Award.objects.filter(movie=movie, festival=1, candidate_type=1))
    cinemaHome_diploma = list(Award.objects.filter(movie=movie, festival=1, candidate_type=2 ))
    simorgh_date = simorgh_awarded[0].date.year
    cinemaHome_date = cinemaHome_awarded[0].date.year
    candidates = len(simorgh_candidate)+len(cinemaHome_candidate)
    awarded = len(simorgh_awarded)+len(cinemaHome_awarded)

    context = {'movie':movie, 'awarded':awarded, 'candidates':candidates, 'simorgh_awarded':simorgh_awarded,
               'simorgh_candidate':simorgh_candidate, 'simorgh_diploma':simorgh_diploma, 'cinemaHome_awarded':cinemaHome_awarded,
                'cinemaHome_candidate':cinemaHome_candidate, 'cinemaHome_diploma':cinemaHome_diploma, 'simorgh_date':simorgh_date,
                'cinemaHome_date':cinemaHome_date}

def search_festival_awards(request):
    pass

def search_festivals_awards_json(request, date, festival_type):

    pass









