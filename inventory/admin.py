# Register your models here.
from django.contrib import admin
from .models import Company, Medicine, Stock, Sell, Inventory


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')

class StockAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'quantity')
    search_fields = ('medicine', 'quantity')

class SellAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'quantity', 'date')
    search_fields = ('medicine', 'date')

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'quantity')
    search_fields = ('medicine', 'quantity')




admin.site.register(Company)
admin.site.register(Medicine)
admin.site.register(Stock)
admin.site.register(Sell)
admin.site.register(Inventory)
