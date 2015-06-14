# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from items.models import Items, Category
from items.forms import CreateOrder, CreateTrash


def catalog(request):
    context = {
        'category': Category.objects.all(),
        'items': Items.objects.order_by('id'),
    }
    return render(request, 'items/catalog.html', context)


def trash(request):
    pass


def order(request):
    pass
