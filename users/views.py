from django.shortcuts import render, get_object_or_404
from .forms import UserForm, UserProfileForm
from .models import User, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email = email, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used email: {} and password: {}".format(email,password))
            return HttpResponse("Invalid login details given")
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return render(request, 'users/login.html', {})

def register(request):
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm
        profile_form = UserProfileForm()
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request,'users/registration.html', context)

def user_profile(request):
    print(request.user)
    if request.user.is_authenticated:
        if request.method == 'POST':
            profile_form_instance = UserProfile.objects.get(user=request.user)
            profile_form = UserProfileForm(request.POST, request.FILES, instance=profile_form_instance)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = request.user
                if 'profile_pic' in request.FILES:
                    profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                return HttpResponseRedirect(reverse('profile'))
            else:
                print(profile_form.errors)
        elif request.method == 'GET':
            obj = UserProfile.objects.get(user=request.user)
            profile_form = UserProfileForm(None, instance=obj)
            profile_picture = UserProfile.objects.get(user_id=request.user.id)
            context = {
                'profile_form': profile_form,
                'profile_picture': profile_picture
            }
            return render(request,'users/profile.html', context)
    else: 
        return HttpResponseRedirect(reverse('home'))
