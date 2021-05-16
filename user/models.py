from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.core.validators import RegexValidator


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    phone = models.CharField(max_length=20 ,validators=[RegexValidator(regex='^(\+98|0)?9\d{9}$)')])
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        self.user= self.user.lower()
        return super().save(*args, **kwargs)


class SupplierProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bank_account = models.CharField('bank account', validators=[RegexValidator(
        regex='^[0-9]{4} [0-9]{4} [0-9]{4} [0-9]{4}$', message='Length has to be more than 8 character')], max_length=255)
    company_name = models.CharField(max_length=500)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state= models.CharField('State/Province/Region: ',max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        self.user= self.user.lower()
        return super().save(*args, **kwargs)


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adrs= models.TextField(max_length=255)

    def __str__(self):
        return f"{self.user.user.email} - {self.adrs}"

    def save(self, *args, **kwargs):
        self.adrs= self.adrs
        return super().save(*args, **kwargs)


