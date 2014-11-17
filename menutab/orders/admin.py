from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

    """docstring for OrderAdmin"""
    list_display = ('user', 'menu_name', 'menu_price',
              'count', 'device_key', 'status','order_time')


admin.site.register(Order, OrderAdmin)
