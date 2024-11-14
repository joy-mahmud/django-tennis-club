from django import forms
from .models import Member

class MemberSearchForm(forms.Form):
    query=forms.CharField()
 
    
class AddMemberForm(forms.ModelForm):
    class Meta:
        model=Member
        fields=["firstname","lastname","age"]
