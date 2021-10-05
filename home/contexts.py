from django.contrib import messages
from .models import Newsletter
from .forms import SubscriptionForm


def subscription_form_contents(request):

    if request.method == 'POST':
        subscription_form = SubscriptionForm(request.POST)
        if subscription_form.is_valid():
            instance = subscription_form.save(commit=False)
            if Newsletter.objects.filter(
                    subscribe_email=instance.subscribe_email).exists():
                messages.error(request,
                               'Sorry, the email already exists in our list')
            else:
                subscription_form.save()
                subscription_form = SubscriptionForm()
                messages.success(request,
                                 'Thank you very much for subscribing \
                                 to our newsletter')
    else:
        subscription_form = SubscriptionForm()

    context = {
        'subscription_form': subscription_form,
        }

    return context
