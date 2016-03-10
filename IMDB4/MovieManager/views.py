
from .models import Movie, Award, Avamel, Reviewer_Review, User_Review, Post, Movie_Celebrity_Image


from django.shortcuts import render
from django.http import HttpResponse




# this function render the main page of each movie and show its detail (e.g. actors, director, ...)
def show_movie(request, id):
    print('before all')
    movie = Movie.objects.get(id=id)
    print('after getting movie')
    reviewer_review_count =Reviewer_Review.objects.filter(movie=movie, show_it=True).count()
    user_review_count = User_Review.objects.filter(movie=movie, show_it=True).count()
    award_simorgh_count = Award.objects.filter(movie=movie, festival=0, candidate_type=0 ).count()
    award_cinemaHome_count = Award.objects.filter(movie=movie, festival=1, candidate_type=0).count()
    candidate_simorgh_count = Award.objects.filter(movie=movie, festival=0, candidate_type=1).count()
    candidate_cinemaHome_count = Award.objects.filter(movie=movie, festival=1, candidate_type=1).count()
    total_candidate_count = candidate_cinemaHome_count+candidate_simorgh_count
    total_award_count = award_cinemaHome_count+award_simorgh_count
    images = movie.images
    actors = movie.get_actors()
    kargardan = list(Avamel.objects.filter(movie=movie, role='kargardan'))
    nevisande = list(Avamel.objects.filter(movie=movie, role='nevisande'))
    tahiey_konande = list(Avamel.objects.filter(movie=movie, role='tahiey_konande'))
    modir_tolid = list(Avamel.objects.filter(movie=movie, role='modir_tolid'))
    mojri_tarh = list(Avamel.objects.filter(movie=movie, role='mojri_tarh'))
    dastyar_aval_kargardan = list(Avamel.objects.filter(movie=movie, role='dastyar_aval_kargardan'))
    barname_riz = list(Avamel.objects.filter(movie=movie, role='barname_riz'))
    modir_film_bardari = list(Avamel.objects.filter(movie=movie, role='modir_film_bardari'))
    tadvin = list(Avamel.objects.filter(movie=movie, role='tadvin'))
    tarrah_sahne_va_lebas = list(Avamel.objects.filter(movie=movie, role='tarrah_sahne_va_lebas'))
    tarrah_chehre_pardazi = list(Avamel.objects.filter(movie=movie, role='tarrah_chehre_pardazi'))
    ahangsaz = list(Avamel.objects.filter(movie=movie, role='ahangsaz'))
    seda_bardari = list(Avamel.objects.filter(movie=movie, role='seda_bardari'))
    seda_Gozari_va_mix = list(Avamel.objects.filter(movie=movie, role='seda_Gozari_va_mix'))
    akkas = list(Avamel.objects.filter(movie=movie, role='akkas'))
    jelvehaye_vije_meydani = list(Avamel.objects.filter(movie=movie, role='jelvehaye_vije_meydani'))
    jelvehaye_vije_basari = list(Avamel.objects.filter(movie=movie, role='jelvehaye_vije_basari'))
    monshi_sahne = list(Avamel.objects.filter(movie=movie, role='monshi_sahne'))
    moshaver_film_name = list(Avamel.objects.filter(movie=movie, role='moshaver_film_name'))
    moshaver_honari = list(Avamel.objects.filter(movie=movie, role='moshaver_honari'))
    moshaver = list(Avamel.objects.filter(movie=movie, role='moshaver'))
    user_review = list(User_Review.objects.filter(movie=movie, show_it=True).order_by(''))
    post = list(Post.objects.filter(movie=movie, show_it=True).order_by('date')[:50])
    context = {'movie':movie, 'reviewer_review_count':reviewer_review_count, 'user_review_count':user_review_count,
               'award_simorgh_count':award_simorgh_count, 'total_award_count':total_award_count
                ,'total_candidate_count':total_candidate_count, 'actors':actors, 'images':images,'kargardan':kargardan, 'nevisande':nevisande,
               'tahiey_konande':tahiey_konande, 'modir_tolid':modir_tolid, 'mojri_tarh':mojri_tarh, 'dastyar_aval_kargardan':dastyar_aval_kargardan,
               'barname_riz':barname_riz, 'modir_film_bardari':modir_film_bardari, 'tadvin':tadvin, 'tarrah_sahne_va_lebas':tarrah_sahne_va_lebas,
               'tarrah_chehre_pardazi':tarrah_chehre_pardazi, 'ahangsaz':ahangsaz, 'seda_bardari':seda_bardari, 'seda_Gozari_va_mix':seda_Gozari_va_mix,
               'akkas':akkas, 'jelvehaye_vije_meydani':jelvehaye_vije_meydani, 'jelvehaye_vije_basari':jelvehaye_vije_basari,
               'monshi_sahne':monshi_sahne, 'moshaver_film_name':moshaver_film_name, 'moshaver_honari':moshaver_honari, 'moshaver':moshaver,
               'user_review':user_review, 'post':post,}
    return render(request, 'movie.html', context=context)






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









