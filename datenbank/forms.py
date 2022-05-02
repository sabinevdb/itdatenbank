from django import forms
from .models import Mitarbeiter

class MitarbeiterForm(forms.ModelForm):

    class Meta:
        model = Mitarbeiter
        fields = ('vorname', 'nachname', 'kontotyp', 'titel', 'mailadresse', 'telefonnummer', 'etage', 'raum', 'serverpasswort', 'adminkonto', 'vpn', 'eintrittsdatum', 'austrittsdatum', 'betreuergruppe', 'bemerkungen', 'konten')
