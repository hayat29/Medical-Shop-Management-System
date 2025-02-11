#view
from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookForm
from .models import Book

def home_view(request):
    return HttpResponse("Welcome to the Medical Shop Management System!")

def book_create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Book created successfully!")
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})


# url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('book/', views.book_create_view, name='book_create'),
]


#models
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
#forms
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title',)

#test
from django.test import TestCase, Client
from django.urls import reverse
from .models import Book
from .forms import BookForm

class HomeViewTest(TestCase):
    def test_home_view_response(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Welcome to the Medical Shop Management System!")

class BookModelTest(TestCase):
    def test_book_title(self):
        book = Book(title="Django for Beginners")
        self.assertEqual(book.title, "Django for Beginners")

class BookFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'title': 'Django for Beginners'}
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'title': ''}
        form = BookForm(data=form_data)
        self.assertFalse(form.is_valid())

class BookCreateViewTest(TestCase):
    def test_book_create_view_get(self):
        client = Client()
        response = client.get(reverse('book_create'))
        self.assertEqual(response.status_code, 200)

    def test_book_create_view_post(self):
        client = Client()
        form_data = {'title': 'Django for Beginners'}
        response = client.post(reverse('book_create'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Book.objects.count(), 1)