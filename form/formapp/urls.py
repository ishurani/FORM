from django.urls import path
from formapp import views

urlpatterns = [
    path('',views.form,name='form'),
    path('students/',views.students)
]
