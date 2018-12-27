# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mainapp.models import ProductCategory, Product, Genres, MusicStyles

admin.site.register (ProductCategory)
admin.site.register (Product)
admin.site.register (Genres)
admin.site.register (MusicStyles)
