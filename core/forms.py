from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'phone', 'address', 'order_details', 'desired_datetime']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (999) 123-45-67'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Полный адрес доставки'}),
            'order_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Опишите состав букета, пожелания, особые указания'}),
            'desired_datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
        labels = {
            'customer_name': 'Имя',
            'phone': 'Телефон',
            'address': 'Адрес доставки',
            'order_details': 'Состав заказа',
            'desired_datetime': 'Желаемые дата и время',
        }