from django.conf.urls import url, patterns


urlpatterns = patterns('users.views',
    url(r'^$', 'profile', name='profile'),
    url(r'^(?P<id>\d+)/$', 'any_profile', name='any_profile'),
)