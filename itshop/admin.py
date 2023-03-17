from django.contrib import admin

# Register your models here.
from .models import Category, Product, Order, Customer

admin.site.register(Category)
# admin.site.register(Customer)


class CustomerAdmin(admin.ModelAdmin):
    def full_name(self):
        return self.first_name + " " + self.last_name

    list_display = (full_name, 'cell', 'email',)
    # list_filter = ('email',),


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purchage_price', 'sell_price', 'discount')
    list_filter = ('category', 'name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'quantity', 'status', )
    list_filter = ('product',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
