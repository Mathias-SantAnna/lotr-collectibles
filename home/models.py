from django.db import models

class Newsletter(models.Model):
    subscribe_email = models.EmailField(max_length=100)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.subscribe_email
