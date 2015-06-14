from django.conf.urls import url, patterns

urlpatterns = patterns('items.views',
    url(r'catalog/$', 'catalog', name='catalog'),
    url(r'trash/$', 'trash', name='trash'),
)