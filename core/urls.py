from django.conf.urls import url, patterns

urlpatterns = patterns('core.views',
    url(r'^(?P<page>\w+)/$', 'static', name='static'),
)