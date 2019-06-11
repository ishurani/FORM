from django.urls import path
from formapp import views

urlpatterns = [
    path('',views.form),
    path('students/',views.students)
]
