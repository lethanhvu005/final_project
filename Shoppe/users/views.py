from ast import Return

from django.shortcuts import render ,redirect
from django.contrib.auth import login ,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm
def RegisterUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.is_superuser=False
            user.is_staff=False
            user.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'register.html',{'form':form})
def LoginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if request.user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})
def LogoutUser(request):
    logout(request)
    return redirect('home')