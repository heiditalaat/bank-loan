from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here


def home(request):
    return render(request, "authentication/index.html")


def signUp(request):

    if request.method == "POST":

        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['password2']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()

        messages.success(
            request, "Your account has been successfully created.")

        return redirect('signIn')

    return render(request, "authentication/signUp.html")


def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, "authentication/index.html", {'firstname': firstname})
        else:
            messages.error(request, 'Bad Credentials :(')
            return redirect('home')

    return render(request, "authentication/signIn.html")


def signOut(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')


def loanProvider(request):
    return render(request, "loanProvider.html")


def createdLoans(request):
    return render(request, "createdLoans.html")


def loanCustomer(request):
    return render(request, "loanCustomer.html")


def bankPersonnel(request):
    return render(request, "bankPersonnel.html")
