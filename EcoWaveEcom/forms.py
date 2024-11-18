from django import forms
from EcoWaveEcom.models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email']