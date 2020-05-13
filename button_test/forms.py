from django import forms
from .models import AppleId


class AppleIdForm(forms.ModelForm):
    class Meta:
        model = AppleId
        fields = '__all__'





