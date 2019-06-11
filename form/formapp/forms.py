from django import forms
from formapp.models import student



class Newstudent(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
        
