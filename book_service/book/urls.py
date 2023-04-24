from django.urls import path
from .views import AuthorListView, PublisherListView, CategoryListView, BookListView, BookDetailView

urlpatterns = [
    path('authors/', AuthorListView.as_view()),
    path('publishers/', PublisherListView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('books/', BookListView.as_view()),
    path('books/<int:id>/', BookDetailView.as_view()),
]
