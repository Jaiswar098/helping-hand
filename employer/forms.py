from django import forms
from .models import Person

class   PersonForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'})) 
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':20}))
    class Meta:
        model = Person
        fields = ('image','title','firstname','lastname','jobtitle','departments','date','email','phone','address',
                  'city','state','pincode')
    
    