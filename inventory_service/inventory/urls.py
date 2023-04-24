from django.urls import path
from .views import ProductListView, ProductDetailView, StockListView, StockDetailView

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:id>/', ProductDetailView.as_view()),
    path('stocks/', StockListView.as_view()),
    path('stocks/<int:id>/', StockDetailView.as_view()),
]
