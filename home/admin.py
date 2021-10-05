from django.contrib import admin
from .models import Newsletter


class SubscribeEmail(admin.ModelAdmin):
    fields = (
        'subscribe_email',
        'subscribed',
    )

    list_display = (
        'subscribe_email', 
        'subscribed',)

admin.site.register(Newsletter, SubscribeEmail) 