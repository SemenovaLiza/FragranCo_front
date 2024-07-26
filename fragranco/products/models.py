from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model


User = get_user_model()


class Products(models.Model):
    title = models.CharField('Product name', max_length=100)
    description = models.TextField('Product description', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2) # let it be 10 millions
    image = models.ImageField(
        'Product image',
        upload_to='products/',
        blank=True, null=True
    )
    buyers = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='bought_products'
    )


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
