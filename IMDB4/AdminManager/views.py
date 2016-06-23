from .models import  Poll,  News, poll_user_choose, PollOption
from CelebrityManager.models import Celebrity
from MovieManager.models import Movie_Celebrity_Image, Teaser, Movie, Avamel

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import JsonResponse
import datetime


def HomePage(request):
    if request.method == "GET":
        teasers = list(Teaser.objects.order_by('date_uploaded')[:3])
        news_iran_cinema = list(News.objects.filter(category='iran_cinema').order_by('-dateUpload')[:5])
        news_world_cinema = list(News.objects.filter(category='world_cinema').order_by('-dateUpload')[:5])
        news_honarmandan = list(News.objects.filter(category='honarmandan').order_by('-dateUpload')[:5])
        news_TV = list(News.objects.filter(category='TV').order_by('-dateUpload')[:5])
        poll = None
        polloptions = None
        try:
            poll = list(Poll.objects.all())[0]
            polloptions = poll.polloption_set.all()
        except:
            pass
        celebrities = Celebrity.get_born_today()
        gallery1 = list(Movie_Celebrity_Image.objects.filter(galleryNumber=1, in_homePage=True)[:5])
        gallery2 = list(Movie_Celebrity_Image.objects.filter(galleryNumber=2, in_homePage=True)[:5])
        gallery3 = list(Movie_Celebrity_Image.objects.filter(galleryNumber=3, in_homePage=True)[:5])
        gallery4 = list(Movie_Celebrity_Image.objects.filter(galleryNumber=4, in_homePage=True)[:5])
        top_sale_movies = list(Movie.objects.filter(is_top_profit=True).order_by('-sale')[0:5])
        top_rated_movies = list(Movie.objects.order_by('-rate')[0:5])
        context = {'Teasers':teasers, 'gallery1':gallery1, 'gallery2':gallery2, 'gallery3':gallery3, 'gallery4':gallery4,
                   'Poll':poll, 'PollOptions':polloptions, 'Celebrity':celebrities, 'News_Iran_Cinema':news_iran_cinema
                    , 'News_World_Cinema':news_world_cinema, 'News_honarmandan':news_honarmandan, 'News_TV':news_TV
                   , 'top_sale_movies':top_sale_movies, 'top_rated_movies':top_rated_movies }
        return render(request, 'AdminManager/index.html', context)


def get_search_result(request, value):
    # movie_serialize = serializers.serialize('json', Movie.objects.filter(name__startswith=value)[0:3])
    # celebrity_serialize = serializers.serialize('json',Celebrity.objects.filter(name__startswith=value)[0:3])
    celebrities = list(Celebrity.objects.filter(name__startswith=value)[0:3])
    movies = list(Movie.objects.filter(name__startswith=value)[0:3])
    name_celebrity = []
    id_celebrity = []
    picture_celebrity = []
    profession_celebrity = []
    for celebrity in celebrities:
        name_celebrity.append(celebrity.name)
        id_celebrity.append(celebrity.id)
        try:
            picture_celebrity.append(celebrity.picture.url)
            profession_celebrity.append(celebrity.workingFields)
        except:
            pass
    name_movie = []
    id_movie = []
    poster_movie = []
    year_movie = []
    director_movie=[]
    for movie in movies:
        name_movie.append(movie.name)
        id_movie.append(movie.id)
        try:
            poster_movie.append(movie.poster.url)
            year_movie.append(movie.year)
            directors = list(Celebrity.objects.filter(agent__movie=movie, agent__role='kargardan'))
            for amel in directors:
                director_movie.append(amel.name)
        except:
            pass
    return JsonResponse({'name_celebrity':name_celebrity,'id_celebrity':id_celebrity,'picture_celebrity':picture_celebrity,
                        'profession_celerity':profession_celebrity,
                         'name_movie':name_movie,'id_movie':id_movie,'poster_movie':poster_movie,'year_movie':year_movie,
                         'director_movie':director_movie})


@login_required()
def Polling(request, poll_id):
    is_voted = False
    poll = Poll.objects.filter(id=poll_id)[0]
    result_polling, total_vote = poll.get_percentage_polling()
    user = request.user
    option_choose = poll_user_choose.objects.filter(poll=poll, user=user)
    if option_choose:
        is_voted = True
    context = {'poll':poll, 'pollOptions':poll.polloption_set.all(), 'is_voted':is_voted ,
                'total_vote':total_vote, 'result_polling':result_polling}
    return render(request, 'AdminManager/polling.html', context)


def PollArchive(request):
    polls = list(Poll.objects.order_by('date'))
    context = {'polls':polls}
    return render(request, 'AdminManager/pollArchive.html', context)


@login_required()
def Polling_result(request, pollOption_number, poll_id):
    poll = Poll.objects.filter(id=poll_id)[0]
    user = request.user
    option_choose = poll_user_choose(user=user, poll=poll, number=pollOption_number)
    option_choose.save()
    poll_option = PollOption.objects.filter(poll=poll, pollNumber=pollOption_number)[0]
    poll_option.rate += 1
    poll_option.save()
    return redirect(reverse('polling', kwargs={"poll_id":poll_id}))



def show_gallery(request, numOfGallery):
    gallery = list(Movie_Celebrity_Image.objects.filter(galleryNumber=numOfGallery))
    context = {'gallery':gallery}
    pass


# this function should be called when the first time user clicks on News button
def show_News_list(request, category):
    news = list(News.objects.filter(category=category).order_by('dateUpload')[0:5])
    count_news = News.objects.filter(category=category).count()
    count_page = int(count_news/5)+1
    top_sale_movies = list(Movie.objects.filter(is_top_profit=True).order_by('-sale')[0:5])
    top_rated_movies = list(Movie.objects.order_by('-rate')[0:5])
    context = {'news':news, 'category':category, 'page_number':1, "count_page":range(count_page), "top_sale_movies":top_sale_movies,
               "top_rated_movies":top_rated_movies}
    return render(request, 'AdminManager/news.html', context)



# this function should be called when user clicks on each page number in news_list_page
def show_news_list_page(request, page, category):
    index_news = (int(page)-1)*5
    news = list(News.objects.filter(category=category).order_by('dateUpload')[index_news:index_news+5])
    count_news = News.objects.filter(category=category).count()
    count_page = int(count_news / 5) + 1
    top_sale_movies = list(Movie.objects.filter(is_top_profit=True).order_by('-sale')[0:5])
    top_rated_movies = list(Movie.objects.order_by('-rate')[0:5])
    context = {'news': news, 'category': category, 'page_number': int(page), "count_page": range(count_page),
               "top_sale_movies": top_sale_movies,
               "top_rated_movies": top_rated_movies}
    return render(request, 'AdminManager/news.html', context)



# this function is used when a news with its conplete text should be showed
def show_news_text(request, news_id):
    news = News.objects.get(id=news_id)
    top_sale_movies = list(Movie.objects.filter(is_top_profit=True).order_by('-sale')[0:5])
    top_rated_movies = list(Movie.objects.order_by('-rate')[0:5])
    context = {'news':news, "top_rated_movies":top_rated_movies, "top_sale_movies":top_sale_movies}
    return render(request, 'AdminManager/newsText.html', context)


















