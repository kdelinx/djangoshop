# coding: utf-8
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.conf import settings
from core.models import Pages
from items.models import Items, Trash

def static(request, page):
    article = get_object_or_404(Pages, page=page)
    context = {
        'txt': Pages.objects.get(page=article.page)
    }
    return render(request, 'core/static.html', context)


def error404(request):
    return render(request, 'core/page404.html', {'message': 'Page not found - 404!'})


def index(request):
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect(
    #         reverse('users:profile')
    #     )
    # else:
    context = {
        'pop_items': Items.objects.order_by('likes', 'counter_buy')[:4],
        'new_items': Items.objects.order_by('-id')[:10],
        'count_buy': Trash.objects.filter(user=request.user.id).count(),
        'name': settings.PROJECT_NAME,
    }
    a = context['pop_items'].query
    print a
    return render(request, 'core/index.html', context)

