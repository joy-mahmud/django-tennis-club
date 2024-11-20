from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from members.models import Member
from members.forms import MemberSearchForm,AddMemberForm,UpdateMemberForm

# Create your views here.

def members_home(request):
 
    context={
        "pageTitle":"Welcome to  members home page",
        "content":"Hello everyone thank you for joining our tennis club",
        "footer":"2024 Your Name"
        }
    return render(request,"home.html",context)
    
def members_about(request):
    context={
        "pageTitle":"Welcome to  members about page",
        "content":"Hello everyone thank you. This is the members about page",
        "footer":"2024 all rights reserved"
        }
    return render(request,'about.html',context)

def add_member(request):
   
    #if request.method=="POST":
        # firstname=request.POST.get("firstname")
        # lastname=request.POST.get("lastname")
        # age=request.POST.get("age")
        # if all([firstname,lastname,age]):
        #     member= Member(firstname=firstname,lastname=lastname,age=age)
        #     member.save()
        #     return HttpResponse("new member added successfully")
    if request.method=="POST":
       form=AddMemberForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("view_members")
    else:
        form=AddMemberForm()
        context={'form':form}
        return render(request,"add_member.html",context)        
    
    

def add_multiple_member(request):
     member1 = Member(firstname='Tobias', lastname='Refsnes')
     member2 = Member(firstname='Linus', lastname='Refsnes')
     member3 = Member(firstname='Lene', lastname='Refsnes')
     member4 = Member(firstname='Stale', lastname='Refsnes')
     members_list = [member1, member2, member3, member4,]
     for x in members_list:
        x.save()
        
     return HttpResponse("multiple member added successfuly")

def add_member_by_url(request):
    firstname=request.GET.get('firstname')
    lastname=request.GET.get('lastname')
    age=request.GET.get('age')
    
    if not all([firstname,lastname,age]):
        return HttpResponse('missing required parameter')
    
    try:
        member=Member.objects.create(firstname=firstname,lastname=lastname,age=age)
        return HttpResponse("new member added successfully")
    except:
        return HttpResponse("something went wrong")
 
def view_members(request):
    members=Member.objects.all().values()
    context={
        "allMembers":members
    }
    return render(request,'view_members.html',context) 
def member_details(request,id):
    member=Member.objects.get(id=id)
    context={
        "member_details":member
    }
    
    return render(request,"member_details.html",context)
    

def search_member(request):
    django_form=MemberSearchForm(request.GET or None)
    searched_member=[]
    if django_form.is_valid():
        query=django_form.cleaned_data.get('query')
        searched_member= Member.objects.filter(firstname=query)
    
    context={
        "members":searched_member,
        "form":django_form
    }
    
    return render(request,'search_member.html',context)

def deleteMember(request,id):
    try:
        member=Member.objects.get(id=id)
        member.delete()
        return redirect('view_members')
    except:
        return HttpResponse("This id doesn't exist")

def updateMember(request,id):
    member=Member.objects.get(id=id)
    
    if request.method == "POST":
        memberForm=UpdateMemberForm(request.POST,instance=member)
        print(request.POST)
        if memberForm.is_valid():
            memberForm.save()
            return redirect('view_members')
        else:
          return HttpResponse('all data are not valid')
            
    memberForm=UpdateMemberForm(instance=member)
    context={
        "form":memberForm
    }
    return render(request,'update_member.html',context)

def testing(request):
    fruits=['apple', 'banana','cherry']
    persons=[
        {
            "firstname": "John",
            "lastname": "Doe",
            "age": 28
        },
        {
            "firstname": "Jane",
            "lastname": "Smith",
            "age": 34
        },
        {
            "firstname": "Michael",
            "lastname": "Brown",
            "age": 42
        },
        {
            "firstname": "Emily",
            "lastname": "Davis",
            "age": 25
        },
        {
            "firstname": "Daniel",
            "lastname": "Wilson",
            "age": 30
        }
        ]

    return JsonResponse({'data':persons})