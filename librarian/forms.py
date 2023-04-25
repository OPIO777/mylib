from django import forms
from django.contrib.auth.models import User
from . import models


class AddNewBookForm(forms.Form):
    name = forms.CharField(max_length=255)
    isbn = forms.IntegerField()
    author = forms.CharField(max_length=255)
    category = forms.CharField(max_length=255)
    subject_area = forms.CharField(max_length=255)


class SForm(forms.Form):
    name = forms.CharField(max_length=255)
    isbn = forms.IntegerField()


class IssueBookForm(forms.Form):
    student_name = forms.CharField(max_length=225)
    student_number = forms.IntegerField()
    name = forms.CharField(max_length=223)
    isbn = forms.IntegerField()
    author = forms.CharField(max_length=225)
    category = forms.CharField(max_length=225)
    subject_area = forms.CharField(max_length=20)



class BorrowForm(forms.Form):
    name = forms.CharField(max_length=255)
    author = forms.CharField()

class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']



class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']


