from .models import UserIMDB, WatchList
from MovieManager.models import RateUserForMovie

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User



def login_page(request):
    errors=''
    print("login page")
    if request.method == "POST":
        print("in if body")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print("in login")
            login(request, user)
            redirect(reversed("AdminManager/homepage"))
        else:
            print("in not login")
            errors="wrong username or password"
    return render(request, "user/login.html", {'errors':errors})



def signup_page(request):
    errors=""
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
    return render(request, "user/signup.html")





def view_profile(request, username):
    print('before all')
    user = User.objects.get(username=username)
    print('after getting user')
    userIMDB = UserIMDB.objects.get(user=user)
    picture_url = userIMDB.get_picture()
    print('after getting picture url: '+picture_url)
    watchList = list(WatchList.objects.filter(user=userIMDB))
    visited_movie = userIMDB.viewed_movie.all
    rated_movie = list(RateUserForMovie.objects.filter(user=user))
    context =  {'user':userIMDB, 'picture_url':picture_url, 'watchList':watchList, 'visited_movie':visited_movie,
                'rated_movie':rated_movie}
    return render(request, 'UserManager/myProfile.html', context)








