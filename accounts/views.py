from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tickets.models import Ticket
from accounts.forms import UserLoginForm, UserRegistrationForm


@login_required
def logout(request):
    """
    Log the user out
    """
    auth.logout(request)
    messages.success(request, "You have successfully been logged out.")
    return redirect(reverse('index'))

def login(request):
    """
    Return a login page and authenticates users
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            # check if user exists
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

            if user:
                # log the user in
                auth.login(user=user, request=request)
                messages.success(request, "You have sucessfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect.")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})

def registration(request):
    """
    Render the registration page
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            # save user to database
            registration_form.save()

            # check if user exists
            user = auth.authenticate(username=request.POST['username'],
                                password=request.POST['password1'])

            if user:
                # log the user in
                auth.login(user=user, request=request)
                messages.success(request, "You have sucessfully registered!")
                return redirect(reverse('index'))
        else:
            messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, "registration.html", {
        "registration_form": registration_form})

def user_profile(request):
    """
    The users profile page
    """
    # retrieve uesr from database
    user = User.objects.get(email=request.user.email)
    tickets = Ticket.objects.filter(user=user)
    return render(request, "profile.html", {"profile": user, 'tickets':tickets})