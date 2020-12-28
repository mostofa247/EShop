from django.db import models
from .category import Category

class product(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category , on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='',null=True,blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return product.objects.filter(category = category_id)
        else:
            return product.get_all_products();