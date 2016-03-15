from .models import  Poll,  News, poll_user_choose, PollOption
from CelebrityManager.models import Celebrity
from MovieManager.models import Movie_Celebrity_Image, Teaser, Movie

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


import datetime


def HomePage(request):
    if request.method == "GET":
        teasers = list(Teaser.objects.order_by('date_uploaded')[:3])
        news_iran_cinema = list(News.objects.filter(category='iran_cinema').order_by('dateUpload')[:5])
        news_world_cinema = list(News.objects.filter(category='world_cinema').order_by('dateUpload')[:5])
        news_honarmandan = list(News.objects.filter(category='honarmandan').order_by('dateUpload')[:5])
        news_TV = list(News.objects.filter(category='TV').order_by('dateUpload')[:5])
        poll = list(Poll.objects.all())[0]
        celebrities = Celebrity.get_born_today()
        gallery1 = list(Movie_Celebrity_Image.objects.filter(galleryNumber=1, in_homePage=True)[:5])
        gallery2 = list(Movie_Celebrity_Image.objects.filter(galleryNumber=2, in_homePage=True)[:5])
        gallery3 = list(Movie_Celebrity_Image.objects.filter(galleryNumber=3, in_homePage=True)[:5])
        gallery4 = list(Movie_Celebrity_Image.objects.filter(galleryNumber=4, in_homePage=True)[:5])
        context = {'Teasers':teasers, 'gallery1':gallery1, 'gallery2':gallery2, 'gallery3':gallery3, 'gallery4':gallery4,
                   'Poll':poll, 'PollOptions':poll.polloption_set, 'Celebrity':celebrities, 'News_Iran_Cinema':news_iran_cinema
                    , 'News_World_Cinema':news_world_cinema, 'News_honarmandan':news_honarmandan, 'News_TV':news_TV }
        return render(request, 'index.html', context)





@login_required()
def Polling(request, poll_id):
    is_voted = False
    poll = Poll.objects.filter(id=poll_id)[0]
    result_polling, total_vote = poll.get_percentage_polling()
    user = request.user
    option_choose = poll_user_choose.objects.filter(poll=poll, user=user)
    if option_choose:
        is_voted = True
    print('is voted: '+str(is_voted))
    context = {'poll':poll, 'pollOptions':poll.polloption_set.all(), 'is_voted':is_voted ,
                'total_vote':total_vote, 'result_polling':result_polling}
    return render(request, 'AdminManager/polling.html', context)



def PollArchive(request):
    polls = list(Poll.objects.order_by('date'))
    for poll in polls:
        print('poll: '+poll.__str__())
    context = {'polls':polls}
    return render(request, 'AdminManager/pollArchive.html', context)


@login_required()
def Polling_result(request, pollOption_number, poll_id):
    print('poll option id: '+str(pollOption_number))
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



def show_News(request, id):
    news = News.objects.filter(id=id)
    time_uploaded_ago = datetime.datetime.now() - news.dateUpload
    context = {'news':news, 'time_uploaded_ago':time_uploaded_ago}
    pass