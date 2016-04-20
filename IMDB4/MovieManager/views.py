
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



    context = {'movie':movie, 'reviewer_review_count':reviewer_review_count, 'user_review_count':user_review_count,
               'award_simorgh_count':award_simorgh_count, 'total_award_count':total_award_count
                ,'total_candidate_count':total_candidate_count, 'actors':actors, 'images':images,'kargardan':kargardan, 'nevisande':nevisande,
               'user_review':user_review, 'posts':posts,}
    return render(request, 'MovieManager/movie.html', context=context)




def show_award_movie(request, id):
    movie = Movie.objects.get(id=id)
    simorgh_awarded = list(Award.objects.filter(movie=movie, festival=0, candidate_type=0))
    simorgh_candidate = list(Award.objects.filter(movie=movie, festival=0, candidate_type=1))
    simorgh_diploma = list(Award.objects.filter(movie=movie, festival=0, candidate_type=2 ))
    cinemaHome_awarded = list(Award.objects.filter(movie=movie, festival=1, candidate_type=0))
    cinemaHome_candidate = list(Award.objects.filter(movie=movie, festival=1, candidate_type=1))
    cinemaHome_diploma = list(Award.objects.filter(movie=movie, festival=1, candidate_type=2 ))
    simorgh_date = None
    if len(simorgh_awarded) is not 0:
        simorgh_date = simorgh_awarded[0].date.year
    cinemaHome_date = None
    if len(cinemaHome_awarded) is not 0:
        cinemaHome_date = cinemaHome_awarded[0].date.year
    candidates = len(simorgh_candidate)+len(cinemaHome_candidate)
    awarded = len(simorgh_awarded)+len(cinemaHome_awarded)
    context = {'movie':movie, 'awarded':awarded, 'candidates':candidates, 'simorgh_awarded':simorgh_awarded,
               'simorgh_candidate':simorgh_candidate, 'simorgh_diploma':simorgh_diploma, 'cinemaHome_awarded':cinemaHome_awarded,
                'cinemaHome_candidate':cinemaHome_candidate, 'cinemaHome_diploma':cinemaHome_diploma, 'simorgh_date':simorgh_date,
                'cinemaHome_date':cinemaHome_date}
    return render(request, 'MovieManager/awards_movie.html', context)


def get_100_best_movies(request):
    movies = list(Movie.objects.order_by('-rate')[:100])
    context = {'movies':movies}
    return render(request, 'MovieManager/top100.html', context)



def search_festival_awards(request):
    list=[]
    years0=[]
    years1=[]
    years2=[]

    years0.append('دوره سی و سوم (۱۳۹۳)')
    years0.append('دوره سی و دوم (۱۳۹۲)')

    years1.append('دوره هفدهم (۱۳۹۴)')
    years1.append('دوره شانزدهم (۱۳۹۳)')
    years1.append('دوره پانزدهم (۱۳۹۲)')

    years2.append('دوره نهم (۱۳۹۴)')
    years2.append('دوره هشتم (۱۳۹۳)')
    years2.append('دوره هفتم (۱۳۹۲)')
    years2.append('دوره ششم (۱۳۹۱)')

    list.append(('جشنواره فیلم فجر',years0))
    list.append(('جشن خانه سینما',years1))
    list.append(('جشن منتقدان سینما',years2))

    context={'list':list}
    return render(request,'MovieManager/festivals.html',context)


def search_festivals_awards_json(request, date, festival_type):
    pass





def sale_table(request):
    movies=list(Movie.objects.order_by('-sale')[:10])
    context={'movies':movies}
    return  render(request,'MovieManager/sale_table.html',context)



def all_crew(request, id):
    movie = Movie.objects.get(id=id)
    avamel = []
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='kargardan')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='nevisande')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='tahiey_konande')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='modir_tolid')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='mojri_tarh')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='dastyar_aval_kargardan')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='barname_riz')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='modir_film_bardari')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='tadvin')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='tarrah_sahne_va_lebas')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='tarrah_chehre_pardazi')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='ahangsaz')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='seda_bardari')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='seda_Gozari_va_mix')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='akkas')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='jelvehaye_vije_meydani')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='jelvehaye_vije_basari')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='monshi_sahne')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='moshaver_film_name')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='moshaver_honari')))
    avamel.append(list(Celebrity.objects.filter(agent__movie=movie, agent__role='moshaver')))
    context = {'movie':movie, 'avamel':avamel}
    return render(request, 'MovieManager/allCrew.html', context)



