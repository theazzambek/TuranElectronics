from django.contrib import admin
from .models import *


class ModelInline(admin.StackedInline):
    model = Model
    extra = 1


class ProductInline(admin.StackedInline):
    model = Product
    extra = 1


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


class CaruselPhotoInline(admin.StackedInline):
    model = CaruselPhoto
    extra = 1


class ColorInline(admin.StackedInline):
    model = Color
    extra = 1


class CharacteristicInline(admin.StackedInline):
    model = Characteristic
    extra = 1


class ReviewsInline(admin.StackedInline):
    model = Reviews
    extra = 1


class SaleInline(admin.StackedInline):
    model = Sale
    extra = 1


class AboutInline(admin.StackedInline):
    model = About
    extra = 1


class NewsInline(admin.StackedInline):
    model = News
    extra = 1


class OrderInline(admin.StackedInline):
    model = Order
    extra = 1


class BasketInline(admin.StackedInline):
    model = Basket
    extra = 1


class FavoriteInline(admin.StackedInline):
    model = Favorite
    extra = 1


class BrandInline(admin.StackedInline):
    model = Brand
    extra = 1


@admin.register(AllModels)
class AllModelsAdmin(admin.ModelAdmin):
    inlines = [ModelInline, ProductInline, PhotoInline, CaruselPhotoInline, ColorInline, CharacteristicInline, ReviewsInline, SaleInline, AboutInline, NewsInline, OrderInline, BasketInline, FavoriteInline, BrandInline]


class ProductAdmin(admin.ModelAdmin):
    exclude = ('allmodels', )


class ModelAdmin(admin.ModelAdmin):
    exclude = ('allmodels', )


class PhotoAdmin(admin.ModelAdmin):
    exclude = ('allmodels',)


class CaruselPhotoAdmin(admin.ModelAdmin):
    exclude = ('allmodels',)


class ColorAdmin(admin.ModelAdmin):
    exclude = ('allmodels',)


class CharacteristicAdmin(admin.ModelAdmin):
    exclude = ('allmodels',)


class ReviewsAdmin(admin.ModelAdmin):
    exclude = ('allmodels',)


class SaleAdmin(admin.ModelAdmin):
    exclude = ('allmodels',)


class AboutAdmin(admin.ModelAdmin):
    exclude = ('allmodels',)


class NewsAdmin(admin.ModelAdmin):
    exclude = ('allmodels',)


class OrderAdmin(admin.ModelAdmin):
    exclude = ('allmodels',)


class BasketAdmin(admin.ModelAdmin):
    exclude = ('allmodels',)


class FavoriteAdmin(admin.ModelAdmin):
    exclude = ('allmodels',)


class BrandAdmin(admin.ModelAdmin):
    exclude = ('allmodels',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(CaruselPhoto, CaruselPhotoAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Model, ModelAdmin)