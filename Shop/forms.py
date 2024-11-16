# forms.py

from django import forms
from .models import Product,Reviews

class ProductForm(forms.ModelForm):
    condition_choices = [
        ('new', 'New'),
        ('like_new', 'Like New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('needs_repair', 'Needs Repair'),
    ]
    trade_in_preference_choices = [
        ('recycle', 'Recycle'),
        ('resell', 'Resell'),
        ('donate', 'Donate'),
    ]

    # Additional Trade-In Fields
    condition = forms.ChoiceField(
        choices=condition_choices,
        widget=forms.Select(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
        }),
        required=True,
    )
    reason_for_trade_in = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            'placeholder': 'Why are you trading in this product?',
            'rows': 3,
        }),
        required=False,
    )
    eco_friendly_certification = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
        }),
        required=False,
    )
    trade_in_preference = forms.ChoiceField(
        choices=trade_in_preference_choices,
        widget=forms.Select(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
        }),
        required=True,
    )
    estimated_value = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            'placeholder': 'Estimated value of the product',
        }),
        required=False,
    )

    class Meta:
        model = Product
        fields = [
            'name', 'description', 'price', 'expiry', 'discount_price',
            'image', 'in_stock', 'condition', 'reason_for_trade_in',
            'eco_friendly_certification', 'trade_in_preference', 'estimated_value'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Sun flower',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Description',
                'rows': 3
            }),
            'price': forms.NumberInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': '0.00',
                'step': '0.01',
                'required': True
            }),
            'expiry': forms.NumberInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': '0',
                'min': 0
            }),
            'discount_price': forms.NumberInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': '0.00',
                'step': '0.01'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }),
            'in_stock': forms.CheckboxInput(attrs={
                'class': 'sr-only peer',
                'id': 'in_stock_toggle'
            }),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['review', 'rating']