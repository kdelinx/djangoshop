from django.conf.urls import url, patterns

urlpatterns = patterns('items.views',
    url(r'catalog/$', 'catalog', name='catalog'),
    url(r'trash/$', 'trash', name='trash'),
    url(r'order/$', 'order', name='order'),
    url(r'like_(?P<id>\d+)/$', 'likes_item', name='likes'),
    url(r'item/(?P<id>\d+)/$', 'item', name='item'),
)
