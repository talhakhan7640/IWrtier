from django.shortcuts import render, redirect
from . forms import UserRegistrationForm
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})



# def login(request):
#     if request.method == "POST":
#         loginForm = UserLoginForm(request.POST)
#         if loginForm.is_valid():
#             return redirect('home')
#     else:
#         loginForm = UserLoginForm()
#     return render(request, 'users/login.html', {'loginForm': loginForm})