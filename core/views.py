from django.shortcuts import render, get_object_or_404
from core.models import Pages

def static(request, page):
    article = get_object_or_404(Pages, page=page)
    context = {
        'txt': Pages.objects.get(page=article.page)
    }
    return render(request, 'core/static.html', context)


def error404(request):
    pass


def index(request):
    pass
