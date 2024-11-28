from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Author,Profile,Book
from .forms import ProfileForm

# Create your views here.

def home(request):
    authors=Author.objects.all()
    data={
        "authors":authors
    }
    return render(request,'library_management/home.html',data)

def addProfile(request,id):
    try:
        author=Author.objects.get(id=id)
        if request.method=="POST":
            profileFormData=ProfileForm(request.POST)
            if profileFormData.is_valid():
                    profile=profileFormData.save(commit=False)
                    profile.author=author
                    profile.save()
                    return redirect('library_home')
                
        else:
            form = ProfileForm()
            context={
            "form":form
            }
        
            return render(request,'library_management/addProfile.html',context)
    except:
       return HttpResponse("something went wrong")    
        
        
def addBook(request):
    author=Author.objects.get(id=2)
    book=Book.objects.create(title="gitanjoli",published_date="1995-04-18",author=author)
    return HttpResponse("book gitanjoli added successfully")
          

def testing(request):
    def addProfile():
       try:
            authoFour=Author.objects.get(id=4)
            author=Author.objects.create(name="author five",email="authorfive@gmail.com")
            profile=Profile.objects.create(
            bio=" new profile author four bio",
            website="https://authorfournew.com",
            birthDate="1990-03-15",
            author=authoFour
            
        ) 
            return HttpResponse("autho five has been created") 
       except:
           return HttpResponse("the profile of this author already exists")
        
    def addAthor():
        author=Author.objects.create(name="author six",email="authorsix@gmail.com")
        return HttpResponse("author six has been added")
    
    # return addAthor()    
    # return addProfile()
    
    def testManyToOneRelation():
        author=Author.objects.get(id=2)
        #books=Book.objects.all()
      
        # for book in books:
            # if book.author_id==author.id:
            #     book_data={
            #         "title":book.title,
            #         "published_date":book.published_date,
            #         "author-name":book.author.name,
            #         "author-email":book.author.email
            #     }
            #     bookList.append(book_data)
            # bookList.append(
            #     {
            #        "title":book.title,
            #        "published_date":book.published_date,
            #        "author-name":book.author.name,
            #        "author-email":book.author.email
            #     }
            # ) 
            
        books=author.books.all()
        print(books)
        bookList=[]
        for book in books:
            bookList.append(
                {
                    "title":book.title,
                    "published":book.published_date
                }
            )
        
                
        return JsonResponse({"books":bookList})
    
    #return testManyToOneRelation()
    
    def testManyToManyRelation():
        author1=Author.objects.get(id=1)
        author2=Author.objects.get(id=2)
        author3=Author.objects.get(id=6)
        
        book=Book.objects.get(id=1)
        book.authors.add(author1,author2,author3)
        authors=[]
        for author in book.authors.all():
            authors.append({
                "name":author.name,
                "email":author.email,
                "bio":author.profile.bio if hasattr(author,'profile') else None,
                "website":author.profile.website if hasattr(author,'profile') else None,
                "birthDate":author.profile.birthDate if hasattr(author,'profile') else None,
            })
        # authors=[{"name":author.name,"email":author.email} for author in book.authors.all()]
        
        return JsonResponse({"authors":authors})
    return testManyToManyRelation()
        
        
        
        
