
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render


def index(request):
    return render(request, "index.html",{})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="home"),
    #path('', include('user.urls')),

]
