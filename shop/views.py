from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['brand_name']


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name_model']


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name_color']


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class CharacteristicViewSet(viewsets.ModelViewSet):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ["product_name"]


class CaruselPhotoViewSet(viewsets.ModelViewSet):
    queryset = CaruselPhoto.objects.all()
    serializer_class = CaruselPhotoSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class AllModelsViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        brands = Brand.objects.all()
        models = Model.objects.all()
        colors = Color.objects.all()
        photos = Photo.objects.all()
        characteristics = Characteristic.objects.all()
        products = Product.objects.all()
        carusels = CaruselPhoto.objects.all()
        favorites = Favorite.objects.all()
        baskets = Basket.objects.all()
        orders = Order.objects.all()
        reviews = Reviews.objects.all()
        news = News.objects.all()
        abouts = About.objects.all()
        sales = Sale.objects.all()

        brand_serializers = BrandSerializer(brands, many=True)
        model_serializers = ModelsSerializer(models, many=True)
        color_serializers = ColorSerializer(colors, many=True)
        photo_serializers = PhotoSerializer(photos, many=True)
        characteristic_serializers = CharacteristicSerializer(characteristics, many=True)
        product_serializers = ProductSerializer(products, many=True)
        carusel_serializers = CaruselPhotoSerializer(carusels, many=True)
        favorite_serializers = FavoriteSerializer(favorites, many=True)
        basket_serializers = BasketSerializer(baskets, many=True)
        order_serializers = OrderSerializer(orders, many=True)
        review_serializers = ReviewsSerializer(reviews, many=True)
        news_serializers = NewsSerializer(news, many=True)
        about_serializers = AboutSerializer(abouts, many=True)
        sale_serializers = SaleSerializer(sales, many=True)

        data = {
            'brands': brand_serializers.data,
            'model': model_serializers.data,
            'color': color_serializers.data,
            'photo': photo_serializers.data,
            'characteristic': characteristic_serializers.data,
            'product': product_serializers.data,
            'carusel': carusel_serializers.data,
            'favorite': favorite_serializers.data,
            'basket': basket_serializers.data,
            'order': order_serializers.data,
            'review': review_serializers.data,
            'news': news_serializers.data,
            'about': about_serializers.data,
            'sale': sale_serializers.data,

        }

        return Response(data)
