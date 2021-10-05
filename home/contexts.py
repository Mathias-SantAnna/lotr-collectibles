from django.conf import settings
from django.contrib import messages
from .forms import SubscriptionForm


def subscription_form_contents(request):

    if request.method == 'POST':
        subscription_form = SubscriptionForm(request.POST)
        if subscription_form.is_valid:
            subscription_form.save()
            messages.success(request, 'Thank you very much for signing up for our newsletter')
    else:
        subscription_form = SubscriptionForm()

    context = {
        'subscription_form': subscription_form,
        }

    return context 