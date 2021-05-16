from django import forms
from .models import SupplierProfile, CustomerProfile, UserAddress
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class CustomerSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['user',
                  'password1', 'password2', 'phone']
        
    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        try:
            user.save()
            CustomerProfile.objects.create(user=user, phone=self.cleaned_data["phone"])

        except Exception as e:
            user.delete()
            raise ValueError(f"cant create profile object! reason: {e}")

        return user


class SupplierSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['user',
                  'password1', 'password2', 'phone']
        
    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        try:
            user.save()
            SupplierProfile.objects.create(user=user, phone=self.cleaned_data["phone"])

        except Exception as e:
            user.delete()
            raise ValueError(f"cant create profile object! reason: {e}")

        return user




