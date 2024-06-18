from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'{self.student} - {self.subject} - {self.grade}'
