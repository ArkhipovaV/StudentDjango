from django import forms
from .models import Student, Subject, Grade

class DateInput(forms.DateInput):
    input_type = 'date'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'birth_date']
        widgets = {
            'birth_date': DateInput(format='%Y-%m-%d'),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'description']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'grade', 'date']
        widgets = {
            'date': DateInput(format='%Y-%m-%d'),
        }
