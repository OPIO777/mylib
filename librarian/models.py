from django.db import models
from datetime import datetime, timedelta

class AddNewBook(models.Model):
    name = models.CharField(max_length=255)
    isbn = models.IntegerField()
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    subject_area = models.CharField(max_length=255)




def get_expiry():
    return datetime.today() + timedelta(days=5)

class IssueBook(models.Model):
    student_name = models.CharField(max_length=225)
    student_number = models.IntegerField()
    name = models.CharField(max_length=223)
    isbn = models.IntegerField()
    author = models.CharField(max_length=225)
    category = models.CharField(max_length=225)
    subject_area = models.CharField(max_length=20)
    issue_date = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField(default=get_expiry)
