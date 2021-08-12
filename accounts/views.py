from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')

def user_sign_up(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user_obj = User.objects.create(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()
        user_auth = authenticate(username=username, password=password)
        login(request, user_auth)

        return redirect('home')
    else:
        return render(request, 'accounts/signup.html')    