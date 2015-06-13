from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import UserCreateForm
from django.utils.translation import ugettext_lazy as _
from users.models import User
from django.contrib.auth.models import Group


class RUserAdmin(UserAdmin):
    form = UserCreateForm
    fieldsets = (
        (_('User'), {'fields': ('email', 'login', 'name', 'first_name', 'telephone',
                                'country', 'city',)}),
        (_('Permissions'),  {'fields': ('is_active', 'is_admin', 'is_superuser',)}),
    )
    list_display = ('id', 'email', 'login', 'telephone', 'country', 'city',)
    list_filter = ('is_admin', 'country', 'city',)
    search_fields = ('email', 'login')
    ordering = ('id',)


admin.autodiscover()
admin.site.register(User, RUserAdmin)
admin.site.unregister(Group)
