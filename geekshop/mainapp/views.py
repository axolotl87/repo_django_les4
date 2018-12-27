# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mainapp.models import ProductCategory, Product, Genres, MusicStyles
from django.shortcuts import render

import json
from django.forms.models import model_to_dict




def index(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    genres = Genres.objects.all()
    music_styles = MusicStyles.objects.all()

    with open('json/product_categories.json', 'w', encoding='utf-8') as tmp_file:
     json.dump(categories, tmp_file)

    # with open('json/genres.json', 'w', encoding='utf-8') as tmp_file:
    #     json.dump(genres, tmp_file)
    #
    # with open('json/music_styles.json', 'w', encoding='utf-8') as tmp_file:
    #     json.dump(music_styles, tmp_file)
    #
    # with open('json/products.json', 'w', encoding='utf-8') as tmp_file:
    #     json.dump(products, tmp_file)
    context = {
        'page_title': 'главная',
        'products': products,
        'categories': categories,
        'genres': genres,
        'music_styles': music_styles,
    }

    return render(request, 'mainapp/index.html', context)





def products(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    genres = Genres.objects.all()
    music_styles = MusicStyles.objects.all()
    context = {
        'page_title': 'каталог',
        'products': products,
        'categories': categories,
        'genres': genres,
        'music_styles': music_styles,
    }
    return render(request, 'mainapp/catalog.html', context)

def product_details(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    genres = Genres.objects.all()
    music_styles = MusicStyles.objects.all()
    context = {
        'page_title': 'товар',
        'products': products,
        'genres': genres,
        'music_styles': music_styles,
        'categories': categories,
    }
    return render(request, 'mainapp/product_details.html', context)


def contacts(request):

    #locations = [
        #     {
        #         'city': 'Москва',
        #         'email': 'info@vinyl-store.com',
        #         'phone': '+7-495-123-45-78',
        #         'address': 'ул. Садовническая д.1',
        #     },
        # ]
        # with open('json/locations.json', 'w', encoding='utf-8') as tmp_file:
        #     json.dump(locations, tmp_file)


    context = {
        'page_title': 'контакты',
        'locations': locations,
    }
    return render(request, 'mainapp/contacts.html', context)




# def base (request):
#    return render (request, 'mainapp/base.html')


# Create your views here.

