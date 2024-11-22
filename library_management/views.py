from django.shortcuts import render
from django.http import HttpResponse
from .models import Author,Profile

# Create your views here.

def home(request):
    return render(request,'library_management/home.html')

def testing(request):
    def addProfile():
       try:
            authoFour=Author.objects.get(id=4)
            author=Author.objects.create(name="name",email="email")
            profile=Profile.objects.create(
            bio=" new profile author four bio",
            website="https://authorfournew.com",
            birthDate="1990-03-15",
            author=authoFour
            
        ) 
            return HttpResponse("autho four has been created") 
       except:
           return HttpResponse("the profile of this author already exists")
        
    
    return addProfile()
        
