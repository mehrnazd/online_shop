from django.urls import path
from .views import ProductDetail,ProductList,Comment

urlpatterns = [
    path('list/',ProductList,name='list'),
    path('detail/',ProductDetail,name='detail'),
    path('comment/',Comment,name='comment'),

]