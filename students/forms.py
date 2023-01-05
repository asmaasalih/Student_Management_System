from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number','first_name','last_name','email','study_field','gpa']
        
        labels = {
            'student_number':'Student Number',
            'first_name': 'First Name',
            'last_name':'Last Name',
            'email': 'Email Address',
            'study_field': 'Study Field',
            'gpa': 'GPA'
        }
        
        widgets = {
            'student_number': forms.NumberInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'study_field':forms.TextInput(attrs={'class':'form-control'}),
            'gpa': forms.NumberInput(attrs={'class':'form-control'})
        }