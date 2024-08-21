from django.contrib import admin
from .models import Category, Image, Brand, Product, Banner, Basket


class BasketAdmin(admin.ModelAdmin):
    readonly_fields = ('unique_code',)


admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Basket, BasketAdmin)
