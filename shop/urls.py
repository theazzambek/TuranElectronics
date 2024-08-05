from django.urls import path
from .views import *

urlpatterns = [
    path("allmodels/", AllModelsViewSet.as_view({"get": "list",  'post': 'create', }), name='brand-list'),
    path('allmodels/<int:pk>/', AllModelsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='brand-detail'),


    path('brands/', BrandViewSet.as_view({'get': 'list', 'post': 'create'}), name='brand-list'),
    path('brands/<int:pk>/', BrandViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='brand-detail'),

    path('models/', ModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='model-list'),
    path('models/<int:pk>/', ModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='model-detail'),

    path('colors/', ColorViewSet.as_view({'get': 'list', 'post': 'create'}), name='color-list'),
    path('colors/<int:pk>/', ColorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='color-detail'),

    path('photos/', PhotoViewSet.as_view({'get': 'list', 'post': 'create'}), name='photo-list'),
    path('photos/<int:pk>/', PhotoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='photo-detail'),

    path('characteristics/', CharacteristicViewSet.as_view({'get': 'list', 'post': 'create'}), name='characteristic-list'),
    path('characteristics/<int:pk>/', CharacteristicViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='characteristic-detail'),

    path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='product-detail'),

    path('caruselphotos/', CaruselPhotoViewSet.as_view({'get': 'list', 'post': 'create'}), name='caruselphoto-list'),
    path('caruselphotos/<int:pk>/', CaruselPhotoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='caruselphoto-detail'),

    path('favourites/', FavoriteViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite-list'),
    path('favourites/<int:pk>/', FavoriteViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='favorite-detail'),

    path('baskets/', BasketViewSet.as_view({'get': 'list', 'post': 'create'}), name='basket-list'),
    path('baskets/<int:pk>/', BasketViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='basket-detail'),

    path('orders/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='order-list'),
    path('orders/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='order-detail'),

    path('reviews/', ReviewsViewSet.as_view({'get': 'list', 'post': 'create'}), name='review-list'),
    path('reviews/<int:pk>/', ReviewsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='review-detail'),

    path('news/', NewsViewSet.as_view({'get': 'list', 'post': 'create'}), name='news-list'),
    path('news/<int:pk>/', NewsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='news-detail'),

    path('about_us/', AboutViewSet.as_view({'get': 'list', 'post': 'create'}), name='about-list'),
    path('about_us/<int:pk>/', AboutViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='about-detail'),

    path('sales/', SaleViewSet.as_view({'get': 'list', 'post': 'create'}), name='sale-list'),
    path('sales/<int:pk>/', SaleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='sale-detail'),
]
