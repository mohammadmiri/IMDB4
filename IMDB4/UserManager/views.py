from .models import UserIMDB, WatchList
from MovieManager.models import RateUserForMovie, Movie
from CelebrityManager.models import Celebrity
from .forms import UserIMDBForms


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse



def login_page(request):
    errors=''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            redirect(reversed("AdminManager/homepage"))
        else:
            errors="wrong username or password"
    return render(request, "user/login.html", {'errors':errors})



def signup_page(request):
    errors=""
    print('before all')
    if request.method == "POST":
        print('after post')
        form = UserIMDBForms(request.POST)
        print('after form: '+form.__str__())
        if form.is_valid():
            print('if valid'+str(request.POST))
            form.save()
            print('after save')
        else:
            print('errors: '+str(form.errors))
            errors = ''
    else:
        form = UserIMDBForms()
    context = {'form':form}
    return render(request, "UserManager/signup.html", context)



def show_suggestion_search_film(request, value):
    films = list(Movie.objects.filter(name__startswith=value).values('name')[0:3])
    return JsonResponse({'films':films})



def show_suggestion_search_celebrity(request, value):
    celebrities = list(Celebrity.objects.filter(name__startswith=value).values('name')[0:3])
    return JsonResponse({'celebrities':celebrities})



def view_profile(request, username):
    user = User.objects.get(username=username)
    userIMDB = UserIMDB.objects.get(user=user)
    picture_url = userIMDB.get_picture()
    watchList = list(WatchList.objects.filter(user=userIMDB))
    visited_movie = userIMDB.viewed_movie.all
    rated_movie = list(RateUserForMovie.objects.filter(user=user))
    context =  {'user':userIMDB, 'picture_url':picture_url, 'watchList':watchList, 'visited_movie':visited_movie,
                'rated_movie':rated_movie}
    return render(request, 'UserManager/myProfile.html', context)



def reset_password(request):
    return


def search_celebrity_sugggestion(request, value):
    celebrities = list(Celebrity.objects.filter(name__startswith=value).values('name')[0:3])
    return JsonResponse({'celebrities':celebrities})


