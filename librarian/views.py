from wsgiref.handlers import format_date_time

from django.shortcuts import render
from .forms import AddNewBookForm, SForm, IssueBookForm,BorrowForm
from .models import AddNewBook, IssueBook, Borrow
from datetime import datetime,timedelta,date
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import auth
from django.contrib.auth.decorators import login_required,user_passes_test

def show(request):
    return render(request,'home.html')


def adding(request):
    title = 'Add Book'
    form = AddNewBookForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        isbn = form.cleaned_data['isbn']
        author = form.cleaned_data['author']
        category = form.cleaned_data['category']
        subject = form.cleaned_data['subject_area']
        p = AddNewBook(name=name, isbn=isbn, author=author, category=category, subject_area=subject)
        p.save()
        return render(request, 'ack.html', {'title':'Book was successfully added'})
    context = {'title': title,
               'form': form,
               }
    return render(request,'adding.html', context)


def existing(request):
    title = 'All available books'
    queryset = AddNewBook.objects.all()

    context = {'title': title,
               'queryset': queryset,
               }
    return render(request, 'existing.html', context)


def search(request):
    title = 'Search Book'
    form = SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        queryset = AddNewBook.objects.filter(name=name)
        context = {'title':title,
                   'queryset': queryset,
                   }
        return render(request,'existing.html',context)

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'search.html', context)


def remove(request):
    title = 'Delete Book'
    form = SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        queryset = AddNewBook.objects.filter(name=name).delete()

        return render(request,'ack.html',{'title': "Book was successfully deleted"})

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'search.html', context)


def issuing(request):
    title = 'Issue Book'
    form = IssueBookForm(request.POST or None)

    if form.is_valid():
        student_name = form.cleaned_data['student_name']
        student_number = form.cleaned_data['student_number']
        name = form.cleaned_data['name']
        isbn = form.cleaned_data['isbn']
        author = form.cleaned_data['author']
        category = form.cleaned_data['category']
        subject = form.cleaned_data['subject_area']


        p = IssueBook(student_name=student_name,student_number=student_number,name=name, isbn=isbn, author=author,
                      category=category, subject_area=subject
                      )
        p.save()
        return render(request, 'ack.html', {'title': 'Book was successfully issued'})
    context = {'title': title,
               'form': form,
               }
    return render(request, 'issuing.html', context)


def issued(request):
    title = 'All Issued  books'
    queryset = IssueBook.objects.all()

    context = {'title': title,
               'queryset': queryset,

               }

    return render(request, 'issued.html', context)




def students(request):
    return render(request,'homa.html')



def avbooks(request):
    title = 'All available books'
    queryset = AddNewBook.objects.all()

    context = {'title': title,
               'queryset': queryset,
               }
    return render(request, 'avbooks.html', context)





