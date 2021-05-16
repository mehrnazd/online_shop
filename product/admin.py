from django.contrib import admin
from .models import Product,Category,Comment


admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Category)