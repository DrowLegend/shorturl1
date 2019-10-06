from django import forms
from shortrurlapp.models import ShortUrls


class UrlForm(forms.ModelForm):
    class Meta:
        model = ShortUrls
        fields = ('url',)
