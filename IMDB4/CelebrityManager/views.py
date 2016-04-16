from .models import Celebrity, Video_Celebrity
from MovieManager.models import Movie, Award
from UserManager.models import PostForCelebrity

from django.shortcuts import render





def show_celebrity(request, id):
    avamels = {}
    celebrity = Celebrity.objects.get(id=id)
    images = list(celebrity.images.all())
    videos = list(celebrity.video_celebrity_set.all())
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

    #adding them to one dictionary
    avamels['movie_kargardan']=movie_kargardan
    avamels['movie_nevisande']=movie_nevisande
    avamels['movie_tahiey_konande']=movie_tahiey_konande
    avamels['movie_modir_tolid']=movie_modir_tolid
    avamels['movie_mojri_tarh']=movie_mojri_tarh
    avamels['movie_Dastyar_aval_kargardan']=movie_Dastyar_aval_kargardan
    avamels['movie_barname_riz']=movie_barname_riz
    avamels['movie_modir_film_bardari']=movie_modir_film_bardari
    avamels['movie_tadvin']=movie_tadvin
    avamels['movie_tarrah_sahne_va_lebas']=movie_tarrah_sahne_va_lebas
    avamels['movie_tarrah_chehre_pardazi']=movie_tarrah_chehre_pardazi
    avamels['movie_ahangsaz']=movie_ahangsaz
    avamels['movie_seda_bardari']=movie_seda_bardari
    avamels['movie_Seda_Gozari_va_mix']=movie_Seda_Gozari_va_mix
    avamels['movie_akkas']=movie_akkas
    avamels['movie_jelvehaye_vije_meydani']=movie_jelvehaye_vije_meydani
    avamels['movie_jelvehaye_vije_basari']=movie_jelvehaye_vije_basari
    avamels['movie_monshi_sahne']=movie_monshi_sahne
    avamels['movie_moshaver_film_name']=movie_moshaver_film_name
    avamels['movie_moshaver_honari']=movie_moshaver_honari
    avamels['movie_moshaver']=movie_moshaver

    context = {'celebrity':celebrity,'images':images, 'movie_actor':movie_actor, 'simorgh_award_count':simorgh_award_count,
               'award_count':award_count, 'candidate_count':candidate_count, 'most_rated_product':most_rated_product,
               'movie_kargardan':movie_kargardan, 'movie_nevisande':movie_nevisande, 'movie_tahiey_konande':movie_tahiey_konande,
               'movie_modir_tolid':movie_modir_tolid, 'movie_mojri_tarh':movie_mojri_tarh, 'videos':videos,
               'movie_Dastyar_aval_kargardan':movie_Dastyar_aval_kargardan, 'movie_barname_riz':movie_barname_riz,
               'movie_modir_film_bardari':movie_modir_film_bardari, 'movie_tadvin':movie_tadvin,
               'movie_tarrah_sahne_va_lebas':movie_tarrah_sahne_va_lebas, 'movie_tarrah_chehre_pardazi':movie_tarrah_chehre_pardazi,
               'movie_ahangsaz':movie_ahangsaz, 'movie_seda_bardari':movie_seda_bardari,
               'movie_Seda_Gozari_va_mix':movie_Seda_Gozari_va_mix, 'avamels':avamels,
               'movie_akkas':movie_akkas, 'movie_jelvehaye_vije_meydani':movie_jelvehaye_vije_meydani,
               'movie_jelvehaye_vije_basari':movie_jelvehaye_vije_basari, 'movie_monshi_sahne':movie_monshi_sahne,
               'movie_moshaver_film_name':movie_moshaver_film_name, 'movie_moshaver_honari':movie_moshaver_honari,
               'movie_moshaver':movie_moshaver, 'posts':posts}
    return render(request, "CelebrityManager/actor.html", context)





def get_awards_celebrity(request, id):
    celebrity = Celebrity.objects.get(id=id)
    simorgh_awarded = list(Award.objects.filter(celebrity=celebrity, festival=0, candidate_type=0))
    simorgh_candidate = list(Award.objects.filter(celebrity=celebrity, festival=0, candidate_type=1))
    simorgh_diploma = list(Award.objects.filter(celebrity=celebrity, festival=0, candidate_type=2 ))
    cinemaHome_awarded = list(Award.objects.filter(celebrity=celebrity, festival=1, candidate_type=0))
    cinemaHome_candidate = list(Award.objects.filter(celebrity=celebrity, festival=1, candidate_type=1))
    cinemaHome_diploma = list(Award.objects.filter(celebrity=celebrity, festival=1, candidate_type=2 ))
    candidates = len(simorgh_candidate)+len(cinemaHome_candidate)
    awarded = len(simorgh_awarded)+len(cinemaHome_awarded)
    context = {'celebrity':celebrity, 'awarded':awarded, 'candidates':candidates, 'simorgh_awarded':simorgh_awarded,
               'simorgh_candidate':simorgh_candidate, 'simorgh_diploma':simorgh_diploma, 'cinemaHome_awarded':cinemaHome_awarded,
                'cinemaHome_candidate':cinemaHome_candidate, 'cinemaHome_diploma':cinemaHome_diploma, }
    return render(request, 'CelebrityManager/awards_actor.html', context)




















