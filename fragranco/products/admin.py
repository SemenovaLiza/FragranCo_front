from django.contrib import admin

from .models import Products


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'image')
    search_fields = ('title',)
    list_filter = ('price',)
    empty_value_display = '-no info-'


admin.site.register(Products)