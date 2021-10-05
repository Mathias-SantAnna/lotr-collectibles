from django import forms
from .models import Newsletter


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('subscribe_email',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False 