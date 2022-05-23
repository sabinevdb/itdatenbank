from django import forms
from .models import Mitarbeiter
from .models import Asset

class MitarbeiterForm(forms.ModelForm):

    class Meta:
        model = Mitarbeiter
        fields = ('vorname', 'nachname', 'kontotyp', 'titel', 'mailadresse', 'telefonnummer', 'etage', 'raum', 'serverpasswort', 'adminkonto', 'vpn', 'eintrittsdatum', 'austrittsdatum', 'betreuergruppe', 'bemerkungen', 'konten', 'assets')

        eintrittsdatum = forms.DateInput()

class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = ('discriminator', 'bestellnummer', 'hersteller', 'haendler', 'raum', 'bemerkung', 'seriennummer', 'mitarbeiterid', 'events')
