from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
# Create your views here.
def userHome(request):
    return render(request,"accounts/user_home.html")

def register(request):
    if request.method=="POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_home')
    else:
        form=UserCreationForm()
        context={
            "form":form
        }
        return render(request,"accounts/register.html",context)
    
def signIn(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('user_home')
        
    else:
        form=AuthenticationForm()
        context={
            'form':form
        }
        return render(request,"accounts/login.html",context)
        