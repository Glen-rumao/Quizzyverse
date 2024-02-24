from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import *


def register(request):
    if request.user.is_authenticated:
        return redirect('profile', request.user.username)


    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['pass1']
        password2 = request.POST['pass2']

        if password == password2:
            # check if email is not same
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Used. Try to Login.")
                return redirect('register')
            
            # check if username is not same
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken.")
                return redirect('register')
            
            else:
                # create user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # log in the user and redirect to profile
                user_login = authenticate(username=username, password=password)
                login(request, user_login)


                # create profile for new user
                user_model = User.objects.get(username=username)
                new_profile = profile.objects.create(user=user_model)
                new_profile.save()
                return redirect('dashboard')
        else:
            messages.info(request, "Password Not Matching.")
            return redirect('register')

    context = {}
    return render(request, "sign-up.html", context)

@login_required(login_url='login_user')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='login_user')
def terms(request):
    return render(request, 'terms-conditions.html')


@login_required(login_url='login_user')
def wallet(request):
    return render(request, 'wallet.html')


@login_required(login_url='login_user')
def prof(request):
    return render(request, 'quiz.html')

@login_required(login_url='login')
def profile_view(request, username):

    # profile user
    user_object2 = User.objects.get(username=username)
    user_profile2 = profile.objects.get(user=user_object2)

    # request user
    user_object = User.objects.get(username=request.user)
    user_profile = profile.objects.get(user=user_object)

    submissions = QuizSubmission.objects.filter(user=user_object2)

    context = {"user_profile": user_profile, "user_profile2": user_profile2, "submissions":submissions}
    return render(request, "profile.html", context)


@login_required(login_url='login')
def editProfile(request):

    user_object = User.objects.get(username=request.user)
    user_profile = profile.objects.get(user=user_object)

    if request.method == "POST":
        # Image
        if request.FILES.get('profile_img') != None:
            user_profile.profile_img = request.FILES.get('profile_img')
            user_profile.save()

        # Email
        if request.POST.get('email') != None:
            u = User.objects.filter(email=request.POST.get('email')).first()

            if u == None:
                user_object.email = request.POST.get('email')
                user_object.save()
            else:
                if u != user_object:
                    messages.info(request, "Email Already Used, Choose a different one!")
                    return redirect('edit_profile')

        # Username
        if request.POST.get('username') != None:
            u = User.objects.filter(username=request.POST.get('username')).first()

            if u == None:
                user_object.username = request.POST.get('username')
                user_object.save()
            else:
                if u != user_object:
                    messages.info(request, "Username Already Taken, Choose an unique one!")
                    return redirect('edit_profile')

        # firstname lastname
        user_object.first_name = request.POST.get('firstname')
        user_object.last_name = request.POST.get('lastname')
        user_object.save()

        # location , bio, gender
        user_profile.location = request.POST.get('location')
        user_profile.gender = request.POST.get('gender')
        user_profile.bio = request.POST.get('bio')
        user_profile.save()

        return redirect('profile', user_object.username)


    context = {"user_profile": user_profile}
    return render(request, 'profile-edit.html', context)


@login_required(login_url='login')
def deleteProfile(request):

    user_object = User.objects.get(username=request.user)
    user_profile = profile.objects.get(user=user_object)

    if request.method == "POST":
        user_profile.delete()
        user_object.delete()
        return redirect('logout')



    context = {"user_profile": user_profile}
    return render(request, 'confirm.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Credentials Invalid!')
            return redirect('login_user')

    return render(request, "sign-in.html")

@login_required(login_url='login_user')
def logout_view(request):
    logout(request)
    return redirect('login_user')


