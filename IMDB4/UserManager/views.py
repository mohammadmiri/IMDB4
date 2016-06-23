from .models import UserIMDB, ListCelebrity, ListMovie
from MovieManager.models import RateUserForMovie, Movie
from CelebrityManager.models import Celebrity
from .forms import UserIMDBForms, MakingListForm
from AdminManager.models import News


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required



# this function is used to show login page and authenticate the user
def login_page(request):
    errors=''
    if request.method == "POST":
        username = request.POST['username']
        print('username: '+username)
        password = request.POST['password']
        print('password: '+password)
        user = authenticate(username=username, password=password)
        print('user: '+str(user))
        if user is not None:
            login(request, user)
            print("after login")
            return redirect('http://localhost:8000/home')
        else:
            errors="wrong username or password"
    else:
        if request.user.is_authenticated():
            return redirect(reverse('UserManager_view_profile', args=[request.user.username]))
    return render(request, "UserManager/login.html", {'errors':errors})


#
# must be fixed later
#
# this function is used to show sign_up and save a new user
def signup_page(request):
    errors=""
    if request.method == "POST":
        form = UserIMDBForms(request.POST)
        print("after creating form")
        if form.is_valid():
            form.save()
            print("reverse: ")
            # return HttpResponseRedirect('http://localhost:8000/home/')
            return redirect('http://localhost:8000/home')
        else:
            errors = ''
    else:
        form = UserIMDBForms()
    context = {'form':form}
    return render(request, 'UserManager/signup.html', context)


# this function should be called by ajax when the user is signing up and choosing his/her amazing film
def show_suggestion_search_film(request, value):
    films = list(Movie.objects.filter(name__startswith=value).values('name')[0:3])
    return JsonResponse({'films':films})


# alaert : there is a function whose job is similar to this function! must be checked later
def search_celebrity_sugggestion(request, value):
    celebrities = list(Celebrity.objects.filter(name__startswith=value).values('name')[0:3])
    return JsonResponse({'celebrities':celebrities})


# this functin is used to show user profile
def view_profile(request, username):
    user = User.objects.get(username=username)
    userIMDB = UserIMDB.objects.get(user=user)
    picture_url = userIMDB.get_picture()
    list_celebrity=ListCelebrity.objects.filter(user=userIMDB).order_by('-date')
    list_movies=ListMovie.objects.filter(user=userIMDB).order_by('-date')
    visited_movie = userIMDB.viewed_movie.all
    rated_movie = list(RateUserForMovie.objects.filter(user=user))
    context =  {'user':userIMDB, 'picture_url':picture_url, 'visited_movie':visited_movie,
                'rated_movie':rated_movie, 'list_celebrity':list_celebrity, 'list_movies':list_movies}
    return render(request, 'UserManager/myProfile.html', context)


# this function is used when the user wants to reset his/her password
def reset_password(request):
    return




# this function is used to show make_list and save a the list created by user
@login_required
def make_list(request, title, category):
    userIMDB = UserIMDB.objects.get(user__username=request.user.username)
    items = []
    error=''
    if request.method=="POST":
        form=MakingListForm()
        error=form.is_valid(request.POST)
        if error=='True':
            form.save()
            redirect(reverse('UserManager_view_profile', request.user.username))
    else:
        if title=='newlist':
            title=''
        else:
            if category == 'movie':
                newlist=ListMovie.objects.filter(title=title).first()
                for item in newlist.movie:
                    items.add(item.name)
            else:
                newlist=ListCelebrity.objects.filter(title=title).first()
                for item in newlist.celebrity:
                    items.add(item.name)
    latest_lists_celebrity = list(ListCelebrity.objects.filter(user=userIMDB).order_by('-date')[0:2])
    latest_lists_movies = list(ListMovie.objects.filter(user=userIMDB).order_by('date')[0:2])
    latest_news = list(News.objects.order_by('-dateUpload'))
    context={'latest_lists_celebrity':latest_lists_celebrity, 'latest_lists_movies':latest_lists_movies, 'latest_news':latest_news,
             "items":items, 'list_name':title, 'error':error}
    return render(request, 'UserManager/make_list.html', context)

