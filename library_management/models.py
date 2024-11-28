from django.db import models

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    def __str__(self) -> str:
        return self.name
    
class Profile(models.Model):
    bio=models.TextField()
    website=models.URLField(null=True,blank=True)
    birthDate=models.DateField(null=True,blank=True)
    author=models.OneToOneField(Author, on_delete=models.CASCADE, related_name="profile")
      
    def __str__(self) -> str:
        return "profile of an author"
class Book(models.Model):
    title=models.CharField(max_length=200)
    published_date=models.DateField()
    #author=models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    authors=models.ManyToManyField(Author, related_name="books")
    