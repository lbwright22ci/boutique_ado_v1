from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def checkout(request):

    bag = request.session.get('bag', ())
    if not bag:
        message.error(request, f'There is nothing in your shopping bag yet.')
        return redirect(reverse('products'))
    
    order_form = OrderForm
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51TbJFNEB7YZrEXaRMuB4Kvgpr3HOmseRkTVJdkODgZtt7s78MVLQR09jrRIdstKLs0iUOpApRnMnNwBZfWJKPx8D00mAPOWFCi',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)