from django import forms
from .models import Mitarbeiter

class MitarbeiterForm(forms.ModelForm):

    class Meta:
        model = Mitarbeiter
        fields = ('vorname', 'nachname',)
