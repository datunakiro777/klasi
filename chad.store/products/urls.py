from django.urls import path
from products.views import ProductViewSet, ReviewViewSet, FavoriteProductViewSet, CartViewSet, TagList, ProductImageViewSet

urlpatterns = [
    path('products/', ProductViewSet.as_view({'get':'list', 'post':'create'}), name="products"),
    path('products/<int:pk>', ProductViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update'}), name='product'),
    path('products/<int:product_id>/images/', ProductImageViewSet.as_view({'get':'list', 'post':'create', 'delete':'destroy'}), name="product-images"),
    path('products/<int:product_id>/images/<int:pk>', ProductImageViewSet.as_view({'get':'retrieve', 'delete':'destroy'}), name="product-image"),
    path('favorite_products/', FavoriteProductViewSet.as_view({'get':'list', 'post':'create', 'delete':'destroy'}), name='favorite_products'),
    path('favorite_products/<int:pk>/', FavoriteProductViewSet.as_view({'get':'retrieve', 'delete':'destroy'}), name='favorite_product'),
    path('products/<int:product_id>/reviews/<int:pk>', ReviewViewSet.as_view(), name="reviews"),
    path('products/<int:product_id>/reviews/', ReviewViewSet.as_view(), name="review"),
    path('cart/', CartViewSet.as_view(), name='cart'),
    path('tags/', TagList.as_view(), name='tags')
]