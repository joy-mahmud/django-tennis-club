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
    author=models.OneToOneField(Author, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return "profile of an author"