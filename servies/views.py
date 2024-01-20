from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .middleware import guest,auth
# Create your views here.

@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()                  #this is save user info
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'','password1':'','password2':''}
        form = UserCreationForm(initial=initial_data)
    return render(request,'register.html',{'form':form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()               #this is get user information
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'','password':''}         # use only password1
        form = AuthenticationForm(initial=initial_data)
    return render(request,'login.html',{'form':form})

@auth
def dashboard_view(request):
    return render(request,'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')