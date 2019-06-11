from django.shortcuts import render
from . import forms


def form(request):
    form=forms.FormName()
    return render(request,'formapp/form.html',{'form':form})

# Create your views here.
