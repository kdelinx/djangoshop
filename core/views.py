# coding: utf-8
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from core.models import Pages
from items.models import Items, Category, Trash

def static(request, page):
    article = get_object_or_404(Pages, page=page)
    context = {
        'txt': Pages.objects.get(page=article.page)
    }
    return render(request, 'core/static.html', context)


def error404(request):
    pass


def index(request):
    context = {
        'pop_items': Items.objects.order_by('likes', 'counter_buy')[:4],
        'new_items': Items.objects.order_by('-id')[:10],
        'count_buy': Trash.objects.filter(user=request.user.id).count(),
    }
    return render(request, 'core/index.html', context)
