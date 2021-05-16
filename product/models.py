from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from user.models import SupplierProfile


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    category = models.ForeignKey(Category , on_delete=models.CASCADE, related_name='product')
    supplier = models.ForeignKey(SupplierProfile, on_delete=models.CASCADE)
    price = models.IntegerField()
    img_one = models.ImageField(upload_to="product/")
    img_two = models.ImageField(upload_to="product/", null=True, blank=True)
    img_three = models.ImageField(upload_to="product/", null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    discount = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    text = models.TextField(null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username


    
