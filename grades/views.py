from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg, Min, Max
from .models import Student, Subject, Grade
from .forms import StudentForm, SubjectForm, GradeForm

def home(request):
    return render(request, 'grades/home.html')

# Student views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'grades/student_list.html', {'students': students})

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'grades/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'grades/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'grades/student_confirm_delete.html', {'student': student})

# Subject views
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'grades/subject_list.html', {'subjects': subjects})

def subject_create(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'grades/subject_form.html', {'form': form})

def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'grades/subject_form.html', {'form': form})

def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        subject.delete()
        return redirect('subject_list')
    return render(request, 'grades/subject_confirm_delete.html', {'subject': subject})

# Grade views
def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'grades/grade_list.html', {'grades': grades})

def grade_create(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'grades/grade_form.html', {'form': form})

def grade_update(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'grades/grade_form.html', {'form': form})

def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == "POST":
        grade.delete()
        return redirect('grade_list')
    return render(request, 'grades/grade_confirm_delete.html', {'grade': grade})

def performance_report(request):
    students = Student.objects.all()
    best_student = students.annotate(avg_grade=Avg('grade__grade')).order_by('-avg_grade').first()
    worst_student = students.annotate(avg_grade=Avg('grade__grade')).order_by('avg_grade').first()

    subjects_avg = Grade.objects.values('subject__name').annotate(avg_grade=Avg('grade'))
    students_avg = Grade.objects.values('student__first_name', 'student__last_name').annotate(avg_grade=Avg('grade'))

    context = {
        'best_student': best_student,
        'worst_student': worst_student,
        'subjects_avg': subjects_avg,
        'students_avg': students_avg
    }
    return render(request, 'grades/performance_report.html', context)
