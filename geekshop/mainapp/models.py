# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Genres (models.Model):
    name = models.CharField(verbose_name='название жанра', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание жанра', blank=True)

    def __str__(self):
        return f'Genres: {self.name} ({self.pk})'

class MusicStyles (models.Model):
    name = models.CharField(verbose_name='название стиля', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание стиля', blank=True)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'MusicStyles: {self.name} ({self.pk})'

class ProductCategory (models.Model):
    name = models.CharField(verbose_name='имя категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание категории товара', blank=True)

    def __str__(self):
        return f'ProductCategory: {self.name} ({self.pk})'

class Product (models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=64, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True)
    music_style = models.ForeignKey(MusicStyles, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Product: {self.name} ({self.pk})'


# Create your models here.
