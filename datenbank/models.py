from django.conf import settings
from django.db import models
from django.utils import timezone



# Create your models here.
class Mitarbeiter(models.Model):
    nachname = models.TextField()
    vorname = models.TextField()
    kontotyp = models.IntegerField(blank=True, null=True)
    titel = models.TextField(blank=True, null=True)
    mailadresse = models.CharField(unique=True, max_length=255, blank=True, null=True)
    telefonnummer = models.CharField(max_length=20, blank=True, null=True)
    etage = models.TextField(blank=True, null=True)
    raum = models.IntegerField(blank=True, null=True)
    standardpasswort = models.BinaryField(blank=True, null=True)
    standardpasswortgesetzt = models.BooleanField(blank=True, null=True)
    serverpasswort = models.TextField(blank=True, null=True)
    adminkonto = models.TextField(blank=True, null=True)
    vpn = models.BooleanField(blank=True, null=True)
    eintrittsdatum = models.DateField(blank=True, null=True)
    austrittsdatum = models.DateField(blank=True, null=True)
    betreuergruppe = models.TextField(blank=True, null=True)
    bemerkungen = models.TextField(blank=True, null=True)
    konten = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mitarbeiter'
