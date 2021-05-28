from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.CustomerSignup.as_view(),name='signup'),
    path('signup_sup/',views.SupplierSignup.as_view() ,name='signup-sup'),
    # path('login/',views.Login,name='login'),
    # path('logout/',views.Logout,'logout'),
    # path('change_pass/', views.change_password, 'change-pass'),
    # path('profile/', views.ShowCustomerProfile, 'profile'),
    # path('edit_profile/', views.EditCustomerProfile, 'edit-profile'),
    

]