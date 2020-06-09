from django.shortcuts import render
from DemoApp.models import Staff,Student
from DemoApp.forms import Student_form
# Create your views here.
def index(request):
    return render(request,'DemoApp/index.html')

def staff(request):
    staff_list=Staff.objects.order_by('teacher_name')
    #staff_dict={'records':staff_list}
    return render(request,'DemoApp/Staff.html',{'records':staff_list})

def student(request):
    form=Student_form()

    if request.POST:
        form=Student_form(request.POST)

        if form.is_valid():
            form.save()

            return index(request)

        else:
            print("Error")

    return render(request,'DemoApp/student.html',{'form':form})

def student_display(request):
    std_list=Student.objects.order_by('student_name')
    return render(request,'DemoApp/student_display.html',{'std':std_list})
