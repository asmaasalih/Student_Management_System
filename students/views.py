from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Student
from .forms import StudentForm


def index(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request,'students/index.html',context)

def view_student(request,id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number'] 
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_study_field = form.cleaned_data['study_field']
            new_gpa = form.cleaned_data['gpa']
            
            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                study_field = new_study_field,
                gpa = new_gpa
                )
            new_student.save()
            return render(request,'students/add_student.html',{'form': StudentForm(),'success':True})
    else:
        form = StudentForm()
        return render(request,'students/add_student.html',{'form': StudentForm()})

def edit_student(request,id):
    student = Student.objects.get(pk=id)
    if request.method == "POST":
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return render(request,'students/edit_student.html',{
                'form': form,
                'success': True
            })
    else:
        form = StudentForm(instance=student)  
        return render(request,'students/edit_student.html',{
            'form':form
        })  
        
def delete_student(request,id):
    if request.method == "POST":
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))            
           
                