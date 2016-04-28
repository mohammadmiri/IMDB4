
from .models import Movie, Award, Avamel, Reviewer_Review, User_Review, Post, Movie_Celebrity_Image, Act, RateUserForMovie
from CelebrityManager.models import Celebrity


from django.shortcuts import render




# this function render the main page of each movie and show its detail (e.g. actors, director, ...)
def show_movie(request, id):
    movie = list(Movie.objects.filter(id=id))[0]
    reviewer_review_count = Reviewer_Review.objects.filter(movie=movie, show_it=True).count()
    user_review_count = User_Review.objects.filter(movie=movie, show_it=True).count()
    award_simorgh_count = Award.objects.filter(movie=movie, festival=0, candidate_type=0 ).count()
    award_cinemaHome_count = Award.objects.filter(movie=movie, festival=1, candidate_type=0).count()
    candidate_simorgh_count = Award.objects.filter(movie=movie, festival=0, candidate_type=1).count()
    candidate_cinemaHome_count = Award.objects.filter(movie=movie, festival=1, candidate_type=1).count()
    total_candidate_count = candidate_cinemaHome_count+candidate_simorgh_count
    total_award_count = award_cinemaHome_count+award_simorgh_count
    images = movie.images.all()
    actors = movie.get_actors()
    # avamel
    kargardan = list(Celebrity.objects.filter(agent__movie=movie, agent__role='kargardan'))
    nevisande = list(Celebrity.objects.filter(agent__movie=movie, agent__role='nevisande'))
    # review
    user_review = list(User_Review.objects.filter(movie=movie, show_it=True).order_by('date'))
    posts = list(Post.objects.filter(movie=movie, show_it=True).order_by('date')[:50])
    #rate
    # user_rate_num=RateUserForMovie.objects.filter(movie=movie, user=request.user)

    context = {'movie':movie, 'reviewer_review_count':reviewer_review_count, 'user_review_count':user_review_count,
               'award_simorgh_count':award_simorgh_count, 'total_award_count':total_award_count
                ,'total_candidate_count':total_candidate_count, 'actors':actors, 'images':images,'kargardan':kargardan, 'nevisande':nevisande,
               'user_review':user_review, 'posts':posts}
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
    avamel.append(('kargardan',list(Celebrity.objects.filter(agent__movie=movie, agent__role='kargardan'))))
    avamel.append(('nevisande',list(Celebrity.objects.filter(agent__movie=movie, agent__role='nevisande'))))
    avamel.append(('tahiey_konande',list(Celebrity.objects.filter(agent__movie=movie, agent__role='tahiey_konande'))))
    avamel.append(('modir_tolid',list(Celebrity.objects.filter(agent__movie=movie, agent__role='modir_tolid'))))
    avamel.append(('mojri_tarh',list(Celebrity.objects.filter(agent__movie=movie, agent__role='mojri_tarh'))))
    avamel.append(('dastyar_aval_kargardan',list(Celebrity.objects.filter(agent__movie=movie, agent__role='dastyar_aval_kargardan'))))
    avamel.append(('barname_riz',list(Celebrity.objects.filter(agent__movie=movie, agent__role='barname_riz'))))
    avamel.append(('modir_film_bardari',list(Celebrity.objects.filter(agent__movie=movie, agent__role='modir_film_bardari'))))
    avamel.append(('tadvin',list(Celebrity.objects.filter(agent__movie=movie, agent__role='tadvin'))))
    avamel.append(('tarrah_sahne_va_lebas',list(Celebrity.objects.filter(agent__movie=movie, agent__role='tarrah_sahne_va_lebas'))))
    avamel.append(('tarrah_chehre_pardazi',list(Celebrity.objects.filter(agent__movie=movie, agent__role='tarrah_chehre_pardazi'))))
    avamel.append(('ahangsaz',list(Celebrity.objects.filter(agent__movie=movie, agent__role='ahangsaz'))))
    avamel.append(('seda_bardari',list(Celebrity.objects.filter(agent__movie=movie, agent__role='seda_bardari'))))
    avamel.append(('seda_Gozari_va_mix',list(Celebrity.objects.filter(agent__movie=movie, agent__role='seda_Gozari_va_mix'))))
    avamel.append(('akkas',list(Celebrity.objects.filter(agent__movie=movie, agent__role='akkas'))))
    avamel.append(('jelvehaye_vije_meydani',list(Celebrity.objects.filter(agent__movie=movie, agent__role='jelvehaye_vije_meydani'))))
    avamel.append(('jelvehaye_vije_basari',list(Celebrity.objects.filter(agent__movie=movie, agent__role='jelvehaye_vije_basari'))))
    avamel.append(('monshi_sahne',list(Celebrity.objects.filter(agent__movie=movie, agent__role='monshi_sahne'))))
    avamel.append(('moshaver_film_name',list(Celebrity.objects.filter(agent__movie=movie, agent__role='moshaver_film_name'))))
    avamel.append(('moshaver_honari',list(Celebrity.objects.filter(agent__movie=movie, agent__role='moshaver_honari'))))
    avamel.append(('moshaver',list(Celebrity.objects.filter(agent__movie=movie, agent__role='moshaver'))))
    acts = Act.objects.filter(movie=movie)
    context = {'movie':movie, 'avamel':avamel, 'acts':acts}
    return render(request, 'MovieManager/allCrew.html', context)



# def festival_awards(request,festival):
#     awards=[]
#     soda_best_movie=[]
#     soda_best_movie_awarded=list(Award.objects.filter(festival=festival, candidate_type=0))
#     soda_best_movie_diploma=list(Award.objects.filter(festival=festival, candidate_type=1))
#     soda_best_movie_candidate=list(Award.objects.filter(festival=festival, candidate_type=2))
#     soda_best_movie.append(('برنده بهترین سیمرغ بلورین',soda_best_movie_awarded))
#     soda_best_movie.append(('دیپلم افتخار',soda_best_movie_diploma))
#     soda_best_movie.append(('نامزد',soda_best_movie_candidate))
#
#     soda_best_director = []
#     soda_best_director_awarded = list(Award.objects.filter(festival=festival, candidate_type=0))
#     soda_best_director_diploma = list(Award.objects.filter(festival=festival, candidate_type=1))
#     soda_best_director_candidate = list(Award.objects.filter(festival=festival, candidate_type=2))
#     soda_best_director.append(('برنده بهترین سیمرغ بلورین', soda_best_director_awarded))
#     soda_best_director.append(('دیپلم افتخار', soda_best_director_diploma))
#     soda_best_director.append(('نامزد', soda_best_director_candidate))
#
#     soda=[]
#     soda.append(('بهترین فیلم',soda_best_movie))
#     soda.append(('بهترین کارگردانی',soda_best_director))
#
#     awards.append(('سودای سیمرغ',soda))
#
#     context={'festival_name':'جشنواره فیلم فجر', 'festival_year':'دوره سی و سوم. ۱۳۹۳', 'awards':awards}
#     return render(request,'MovieManager/festival_awards.html',context)























