from django.db import models

class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=10)
    sclass=models.IntegerField(max_length=10)
    sjd=models.DateField()
    scd=models.DateField()