from django.shortcuts import render
from formapp.forms import Newstudent
from formapp.models import student

def index(request):
    return render(request,'formapp/index.html')




def form(request):
    form = Newstudent()

    if request.method == "POST":
      form = Newstudent(request.POST, request.FILES)

      if form.is_valid():
          form.save(commit=True)
          return render(request,'formapp/index.html')
      else:
         print('Error')
    return render(request,'formapp/form.html',{'form':form})


def students(request):
    if request.method == 'GET':

            student_list=student.objects.order_by('name')
            student_dict={'Students':student_list}
            return render(request,'formapp/students.html',context=student_dict)





# Create your views here.
