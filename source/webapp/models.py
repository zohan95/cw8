from math import modf

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

PRODUCT_CATEGORY = (
    ('fruits', "Фрукты"),
    ("wear", "Одежда"),
    ("other", "Другое")
)


class Product(models.Model):
    name = models.CharField(max_length=63, verbose_name='Название')
    category = models.CharField(max_length=63, choices=PRODUCT_CATEGORY, default=PRODUCT_CATEGORY[2][0],
                                verbose_name='Категории')

    description = models.TextField(max_length=300, verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Картинка товара')

    def __str__(self):
        return self.name

    @property
    def mid_rating(self):
        mid_rate = 0
        review = Review.objects.filter(product__name=self.name).filter(product__category=self.category).filter(
            product__description=self.description)
        for i in review:
            mid_rate += i.mark
        if mid_rate:
            mid_rate = mid_rate / len(review)
        a, b = modf(mid_rate)
        print(a)
        return a, range(int(b))


class Review(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', related_name='review_user', on_delete=models.PROTECT)
    product = models.ForeignKey('Product', related_name='review_product', verbose_name='Товар',
                                on_delete=models.CASCADE)
    review_text = models.TextField(max_length=511, verbose_name='Текст отзыва')
    mark = models.PositiveIntegerField(default=5,
                                       validators=[
                                           MaxValueValidator(5),
                                           MinValueValidator(1)
                                       ])

    @property
    def get_range(self):
        return range(self.mark)
