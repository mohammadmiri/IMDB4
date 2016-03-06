from .models import UserIMDB

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





def view_profile(request, name):
    user = request.user
    userIMDB = UserIMDB.objects.filter(user=user)
    return render(request, 'user/profile.html', {'user':userIMDB})








