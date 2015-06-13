from django.contrib import admin
from items.models import Items, Category, Gallery, Color, Order, Trash, Sizes, Travel, Payment


class RItemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'descriptions', 'balance',)
    list_filter = ('id', 'title', 'probe', 'likes', 'price', 'price_per_gramm',
                   'balance', 'counter_buy', 'color', 'categories',)
    save_on_top = True
    ordering = ('balance', 'probe', 'weight',)


class ROrderAdmin(admin.ModelAdmin):
    list_filter = ('id', 'number', 'user', 'various', 'index', 'status',)
    list_display = ('number', 'user', 'date_expiries', 'telephone',)
    ordering = ('number', '-user', 'status')
    save_on_top = True

class RTrashAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'count', 'user', 'number')
    list_filter = ('id', 'count', 'user',)
    ordering = ('id', '-count',)
    save_on_top = True


admin.site.register(Items, RItemsAdmin)
admin.site.register(Category)
admin.site.register(Gallery)
admin.site.register(Color)
admin.site.register(Order, ROrderAdmin)
admin.site.register(Trash, RTrashAdmin)
admin.site.register(Sizes)
admin.site.register(Travel)
admin.site.register(Payment)
