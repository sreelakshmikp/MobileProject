from django.forms import ModelForm
from .models import Product,Order,Cart
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateProductForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        widgets={
            'product_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Product Name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'specs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Specs'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'})
        }

    def clean(self):
        print("validation here")

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2","email"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=["user","product","address"]
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User'}),
            'product': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Product'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address'})
        }

class CartForm(ModelForm):
    class Meta:
        model=Cart
        fields="__all__"
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User'}),
            'product': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Product'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
        }
