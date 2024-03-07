from django.contrib import admin

from .models import Product, Costumer

# Exibindo na opçao produtos (admin) nome, preço e estoque
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

# Exibindo na opçaõ usuarios, o nome, sobrenome e estoque
class CostumerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email')


admin.site.register(Product, ProductAdmin)
admin.site.register(Costumer, CostumerAdmin)
