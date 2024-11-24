from django import forms 
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','website','birthDate']
        widgets={
            'birthDate':forms.DateInput(attrs={'type':'date'})
        }
       