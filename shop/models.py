from django.contrib.auth.models import User
from django.db import models


class AllModels(models.Model):
    pass


class Brand(models.Model):
    brand_name = models.CharField(max_length=60)
    photo = models.ImageField(upload_to="images/brand/", blank=True, null=True)
    allmodels = models.ForeignKey(AllModels, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.brand_name


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
    name_model = models.CharField(max_length=32, unique=True)
    allmodels = models.ForeignKey('AllModels', on_delete=models.CASCADE, related_name='all_model', null=True,
                                  blank=True)
    def __str__(self):
        return self.name_model


class Color(models.Model):
    name_color = models.CharField(max_length=50)
    allmodels = models.ForeignKey('AllModels', on_delete=models.CASCADE, related_name='all_color', null=True,
                                  blank=True)

    def __str__(self):
        return self.name_color


class Photo(models.Model):
    image = models.ImageField(upload_to='product_photos/', verbose_name='фото продукта')
    name_photo = models.CharField(max_length=300)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='photo', null=True, blank=True)
    allmodels = models.ForeignKey('AllModels', on_delete=models.CASCADE, related_name='all_photo', null=True,
                                blank=True)

class Characteristic(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='characteristics')
    key = models.CharField(max_length=255, verbose_name="Название обьёма")
    value = models.CharField(max_length=255)
    allmodels = models.ForeignKey('AllModels', on_delete=models.CASCADE, related_name='all_character', null=True,blank=True)
    def __str__(self):
        return f"{self.key}: {self.value}"


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1, related_name='brand')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, default=1, related_name='model')
    product_name = models.CharField(max_length=100, verbose_name='название продукта')
    description = models.TextField(verbose_name='описание')
    color = models.ManyToManyField(Color, blank=True, verbose_name="Цвет")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    photos = models.ManyToManyField(Photo, blank=True, verbose_name='фото продукта', related_name='photos')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)],
                                default=1, verbose_name="Оценка")
    data = models.DateField(auto_now=True, blank=True, null=True)
    allmodels = models.ForeignKey('AllModels', on_delete=models.CASCADE, related_name='all_product', null=True, blank=True)

    def __str__(self):
        return self.product_name


class CaruselPhoto(models.Model):
    photo = models.ImageField(upload_to="images/carusel/", blank=True, null=True)
    carusel_title = models.TextField(default="Default Title")
    allmodels = models.ForeignKey('AllModels', on_delete=models.CASCADE, related_name='all_carusel', null=True,blank=True)

    def __str__(self):
        return self.carusel_title


class Favorite(models.Model):
    user_favorite = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    allmodels = models.ForeignKey('AllModels', on_delete=models.CASCADE, related_name='all_favorite', null=True,blank=True)

    def __str__(self):
        return self.user_favorite


class Basket(models.Model):
    user_basket = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_basket', default=1)
    count = models.PositiveIntegerField(verbose_name='количество товара', default=1)
    summ_products = models.IntegerField(verbose_name="общая сумма")
    allmodels = models.ForeignKey('AllModels', on_delete=models.CASCADE, related_name='all_basket', null=True,blank=True)

    def __str__(self):
        return self.user_basket


class Order(models.Model):
    user_order = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Basket)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    allmodels = models.ForeignKey('AllModels', on_delete=models.CASCADE, related_name='all_order', null=True,blank=True)

    def __str__(self):
        return self.user_order


class Reviews(models.Model):
    user_reviews = models.ForeignKey(User, models.CASCADE)
    text_reviews = models.TextField()
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    product = models.ForeignKey(Product, verbose_name="продукт", on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)],
                                help_text="Rate the item with 0 to 6 stars.", verbose_name="Rating")
    data = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.user_reviews
    allmodels = models.ForeignKey('AllModels', on_delete=models.CASCADE, related_name='all_review', null=True,blank=True)


class News(models.Model):
    name_news = models.CharField(max_length=500)
    description = models.TextField()
    photo = models.ImageField(upload_to="images/news/", blank=True, null=True)
    data = models.DateField(auto_now=True, blank=True, null=True)
    allmodels = models.ForeignKey('AllModels', on_delete=models.CASCADE, related_name='all_news', null=True,blank=True)

    def __str__(self):
        return self.name_news


class About(models.Model):
    text_about = models.TextField()
    allmodels = models.ForeignKey('AllModels', on_delete=models.CASCADE, related_name='all_about', null=True,blank=True)

    def __str__(self):
        return self.text_about


class Sale(models.Model):
    number = models.IntegerField(choices=[(i, str(i)) for i in range(1, 101)],
                                help_text="Можно писать до 100", verbose_name="Sales")
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name="product")
    allmodels = models.ForeignKey('AllModels', on_delete=models.CASCADE, related_name='all_sale', null=True,blank=True)

    def __str__(self):
        return f"{self.number} - {self.product}"


