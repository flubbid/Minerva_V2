from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Student(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField(default=None)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('students_detail', kwargs={'pk': self.id})


class Assignment(models.Model):
    CATEGORY = (
        ('NONE', 'None'),
        ('ENG', 'English'),
        ('MATH', 'Mathematics'),
        ('LANG', 'Language'),
        ('HIST', 'History'),
        ('SCI', 'Science')
    )
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY,
        default=CATEGORY[0][0]
        )
    description = models.TextField(max_length=250)
    due_date = models.DateField('due date')
    students = models.ManyToManyField(Student)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'assignment_id': self.id})

    class Meta:
        ordering = ['-due_date']

