from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	age = models.IntegerField()
	gender = models.CharField(max_length=3)

	def __str__(self):
		return self.first_name + self.last_name

class Grades(models.Model):
	student = models.ForeignKey(Student)
	sgpa = models.CharField(max_length=10)
	cgpa = models.CharField(max_length=10)

	def __str__(self):
		return self.student.first_name+ self.student.last_name
