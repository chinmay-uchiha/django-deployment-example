from django.db import models

# Create your models here.
class Staff(models.Model):
    teacher_name=models.CharField(max_length=20)
    teacher_no=models.IntegerField()
    teacher_email=models.EmailField()

    def __str__(self):
        return self.teacher_name

class Subject(models.Model):
    subject_name=models.CharField(max_length=20)

    def __str__(self):
        return self.subject_name


class Student(models.Model):
    student_name=models.CharField(max_length=20)
    student_no=models.IntegerField()
    alt_student_no=models.IntegerField()
    studet_subjects=models.ForeignKey(Subject,on_delete=models.CASCADE)
