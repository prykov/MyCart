from django import forms
from .models import *


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class UserProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['cart']


class CartForm(forms.ModelForm):

    class Meta:
        model = Cart
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2})
        }


class UserCartForm(forms.ModelForm):

    class Meta:
        model = Cart
        fields = ('name', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2})
        }
