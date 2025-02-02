from django.urls import path
from products.views import product_view, review_view, get_product

urlpatterns = [
    path('products/', product_view, name="products"),
    path('reviews/', review_view, name="reviews"),
    path('products/<int:pk>/', get_product, name='product')
]