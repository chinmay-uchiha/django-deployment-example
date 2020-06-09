from django import forms
from DemoApp.models import Student,Subject

class Student_form(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
