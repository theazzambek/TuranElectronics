from rest_framework.serializers import ModelSerializer
from .models import *


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ModelsSerializer(ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'

class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class CharacteristicSerializer(ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CaruselPhotoSerializer(ModelSerializer):
    class Meta:
        model = CaruselPhoto
        fields = '__all__'

class FavoriteSerializer(ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class BasketSerializer(ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ReviewsSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class SaleSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
