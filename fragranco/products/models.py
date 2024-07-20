from django.db import models


class Products(models.Model):
    title = models.CharField('Product name', max_length=100)
    description = models.TextField('Product description', blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(
        'Product image',
        upload_to='products/',
        blank=True, null=True
    )


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
