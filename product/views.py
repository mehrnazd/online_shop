from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView

from .models import Product,Category,Comment 

class ProductList(ListView):
    model = Product
    template_name = "shop.html"
    context_object_name = 'product'
    paginate_by = 2

    



class ProductDetail(DetailView):
    model = Product
    template_name = "shop_detail.html"
    context_object_name = 'product'


class Comment():
    pass


class DeleteComment():
    pass