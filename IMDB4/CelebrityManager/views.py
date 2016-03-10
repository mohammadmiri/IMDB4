from .models import Celebrity
from MovieManager.models import Movie, Award
from UserManager.models import PostForCelebrity

from django.shortcuts import render





def show_celebrity(request, name):
    celebrity = Celebrity.objects.get(name= name)
    images = celebrity.get_images()
    movie_actor = Movie.get_movie_act(celebrity)
    # get count of awards
    simorgh_award_count = Award.get_festival_award_count(cele=celebrity, festival=0, candidate_type=0)
    award_count = Award.get_award_count(cele=celebrity, candidate_type=0)
    candidate_count = Award.get_award_count(cele=celebrity, candidate_type=1)
    # getting most rated movie
    most_rated_product = Celebrity.get_most_rated_film(celebrity)
    # getting movie actor
    movie_actor = Movie.get_movie_act(cele=celebrity)
    # getting movies being one of its avamel
    movie_kargardan = Movie.objects.filter(agent__role='kargardan', agent__celebrity=celebrity)
    movie_nevisande = Movie.objects.filter(agent__role='nevisande', agent__celebrity=celebrity)
    movie_tahiey_konande = Movie.objects.filter(agent__role='tahiey_konande', agent__celebrity=celebrity)
    movie_modir_tolid = Movie.objects.filter(agent__role='modir_tolid', agent__celebrity=celebrity)
    movie_mojri_tarh = Movie.objects.filter(agent__role='mojri_tarh', agent__celebrity=celebrity)
    movie_Dastyar_aval_kargardan = Movie.objects.filter(agent__role='Dastyar_aval_kargardan', agent__celebrity=celebrity)
    movie_barname_riz = Movie.objects.filter(agent__role='barname_riz', agent__celebrity=celebrity)
    movie_modir_film_bardari = Movie.objects.filter(agent__role='modir_film_bardari', agent__celebrity=celebrity)
    movie_tadvin = Movie.objects.filter(agent__role='tadvin', agent__celebrity=celebrity)
    movie_tarrah_sahne_va_lebas = Movie.objects.filter(agent__role='tarrah_sahne_va_lebas', agent__celebrity=celebrity)
    movie_tarrah_chehre_pardazi = Movie.objects.filter(agent__role='tarrah_chehre_pardazi', agent__celebrity=celebrity)
    movie_ahangsaz = Movie.objects.filter(agent__role='ahangsaz', agent__celebrity=celebrity)
    movie_seda_bardari = Movie.objects.filter(agent__role='seda_bardari', agent__celebrity=celebrity)
    movie_Seda_Gozari_va_mix = Movie.objects.filter(agent__role='Seda_Gozari_va_mix', agent__celebrity=celebrity)
    movie_akkas = Movie.objects.filter(agent__role='akkas', agent__celebrity=celebrity)
    movie_jelvehaye_vije_meydani = Movie.objects.filter(agent__role='jelvehaye_vije_meydani', agent__celebrity=celebrity)
    movie_jelvehaye_vije_basari = Movie.objects.filter(agent__role='jelvehaye_vije_basari', agent__celebrity=celebrity)
    movie_monshi_sahne = Movie.objects.filter(agent__role='monshi_sahne', agent__celebrity=celebrity)
    movie_moshaver_film_name = Movie.objects.filter(agent__role='moshaver_film_name', agent__celebrity=celebrity)
    movie_moshaver_honari = Movie.objects.filter(agent__role='moshaver_honari', agent__celebrity=celebrity)
    movie_moshaver = Movie.objects.filter(agent__role='moshaver', agent__celebrity=celebrity)
    # getting posts of users
    posts = PostForCelebrity.objects.filter()

    context = {}
    return render(request, "CelebrityManager/actor.html", context)
























