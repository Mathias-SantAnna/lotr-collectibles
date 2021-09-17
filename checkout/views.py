from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in the shopping bag at the moment')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JaYIrAhzIwDcH5c4OZaxixkJcRNBacR2j0Lahh9LJVlcfzXxMPta5HpErZN2RTHcJUp3N2k9AGXclaAH1HrYPH800oJYoz6LS',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)