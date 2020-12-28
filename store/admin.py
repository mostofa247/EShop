from django.contrib import admin
from .models.product import product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class Adminproduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']



class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(product,Adminproduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order )
