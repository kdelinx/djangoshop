# coding: utf-8
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from items.models import Items, Category
from users.models import User
from items.forms import CreateOrder, CreateTrash


def catalog(request):
    context = {
        'category': Category.objects.all(),
        'items': Items.objects.order_by('id'),
    }
    return render(request, 'items/catalog.html', context)


def trash(request):
    context = {
        'form': CreateTrash(request.POST or None)
    }
    return render(request, 'items/trash.html', context)


def order(request):
    context = {
        'form': CreateOrder(request.POST or None)
    }
    return render(request, 'items/order.html', context)


def likes_item(request, id):
    item = get_object_or_404(Items, id=id)
    user = get_object_or_404(User, request.user.id)
    if user in item:
        item.likes.add()
        messages.success(request, 'Товар одобрен')
    else:
        item.likes.remove()
        messages.error(request, 'Одобрение отвергнуто')
    return HttpResponseRedirect(
        reverse('items:catalog')
    )
