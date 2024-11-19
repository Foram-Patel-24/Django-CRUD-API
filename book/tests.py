from django.test import TestCase
from .models import Book
from datetime import date


class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Author Name",
            published_date=date(2023, 1, 1)
        )

    # book is created successfully
    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Author Name")

    # __str__ method of the Book model
    def test_book_string_representation(self):
        self.assertEqual(str(self.book), "Test Book")



