from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderForm
from .models import Order

def home(request):
    return render(request, 'core/home.html')

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            messages.success(request, f'Заказ #{order.id} успешно оформлен! Мы свяжемся с вами для подтверждения.')
            return redirect('home')
    else:
        form = OrderForm()
    
    return render(request, 'core/order_form.html', {'form': form})