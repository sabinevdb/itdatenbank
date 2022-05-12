from django.conf import settings
from django.db import models
from django.utils import timezone



# Create your models here.
class Asset(models.Model):
    discriminator = models.CharField(max_length=50, blank=True, null=True)
    bestellnummer = models.IntegerField(blank=True, null=True)
    hersteller = models.CharField(max_length=130, blank=True, null=True)
    haendler = models.CharField(max_length=130, blank=True, null=True)
    raum = models.IntegerField(max_length=50, blank=True, null=True)
    bemerkung = models.TextField(blank=True, null=True)
    seriennummer = models.CharField(max_length=130, blank=True, null=True)
    mitarbeiterid = models.ForeignKey('Mitarbeiter', models.DO_NOTHING, db_column='mitarbeiterid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset'

    def __str__ (self):
        return self.discriminator + ', ' + self.bestellnummer

class Controller(models.Model):
    id = models.OneToOneField('Komponente', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'controller'


class Cpu(models.Model):
    id = models.OneToOneField('Komponente', models.DO_NOTHING, db_column='id', primary_key=True)
    taktfrequenz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cpu'


class Dockingstation(models.Model):
    id = models.OneToOneField('Hardware', models.DO_NOTHING, db_column='id', primary_key=True)
    mac = models.TextField(blank=True, null=True)  # This field type is a guess.
    junetip = models.GenericIPAddressField(blank=True, null=True)
    junetname = models.TextField(blank=True, null=True)
    notebookid = models.ForeignKey('Notebook', models.DO_NOTHING, db_column='notebookid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dockingstation'


class Drucker(models.Model):
    id = models.OneToOneField('Hardware', models.DO_NOTHING, db_column='id', primary_key=True)
    internetnummer = models.GenericIPAddressField(blank=True, null=True)
    speicher = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drucker'


class Dvdlaufwerk(models.Model):
    id = models.OneToOneField('Komponente', models.DO_NOTHING, db_column='id', primary_key=True)
    geschwindigkeit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dvdlaufwerk'


class Event(models.Model):
    event = models.IntegerField(blank=True, null=True)
    datum = models.DateTimeField(blank=True, null=True)
    assetid = models.ForeignKey(Asset, models.DO_NOTHING, db_column='assetid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class Grafikkarte(models.Model):
    id = models.OneToOneField('Komponente', models.DO_NOTHING, db_column='id', primary_key=True)
    speicher = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grafikkarte'


class Hardware(models.Model):
    id = models.OneToOneField(Asset, models.DO_NOTHING, db_column='id', primary_key=True)
    inventarnummer = models.IntegerField(unique=True, blank=True, null=True)
    bezeichnung = models.TextField(blank=True, null=True)
    schnittstellen = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hardware'


class Hauptspeicher(models.Model):
    id = models.OneToOneField('Komponente', models.DO_NOTHING, db_column='id', primary_key=True)
    groesse = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hauptspeicher'


class Internefestplatte(models.Model):
    id = models.OneToOneField('Komponente', models.DO_NOTHING, db_column='id', primary_key=True)
    groesse = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internefestplatte'


class Komponente(models.Model):
    id = models.OneToOneField(Asset, models.DO_NOTHING, db_column='id', primary_key=True)
    modell = models.TextField(blank=True, null=True)
    bus = models.TextField(blank=True, null=True)
    rechnerid = models.ForeignKey('Rechner', models.DO_NOTHING, db_column='rechnerid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'komponente'


class Mitarbeiter(models.Model):

    class KontoTyp(models.TextChoices):
        NNAKTIV = 1, 'Noch nicht aktiv'
        AKTIV = 2, 'Aktiv'
        AUSGESCHIEDEN = 3, 'Ausgeschieden'
        EXTERN = 4, 'Extern'

    nachname = models.CharField(max_length=130)
    vorname = models.CharField(max_length=130)
    # kontotyp = models.IntegerField(blank=True, null=True)
    kontotyp = models.IntegerField(blank=True, null=True, choices=KontoTyp.choices, default=KontoTyp.NNAKTIV)
    titel = models.CharField(max_length=130, blank=True, null=True)
    mailadresse = models.CharField(unique=True, max_length=255, blank=True, null=True)
    telefonnummer = models.CharField(max_length=20, blank=True, null=True)
    etage = models.CharField(max_length=20, blank=True, null=True)
    raum = models.IntegerField(max_length=20, blank=True, null=True)
    standardpasswort = models.BinaryField(max_length=20, blank=True, null=True)
    standardpasswortgesetzt = models.BooleanField(blank=True, null=True)
    serverpasswort = models.CharField(max_length=20, blank=True, null=True)
    adminkonto = models.CharField(max_length=20, blank=True, null=True)
    vpn = models.BooleanField(blank=True, null=True)
    eintrittsdatum = models.DateField(blank=True, null=True)
    austrittsdatum = models.DateField(blank=True, null=True)
    betreuergruppe = models.CharField(max_length=130, blank=True, null=True)
    bemerkungen = models.TextField(blank=True, null=True)
    konten = models.CharField(max_length=130, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mitarbeiter'

    def __str__ (self):
        return self.nachname + ', ' + self.vorname

class Monitor(models.Model):
    id = models.OneToOneField(Hardware, models.DO_NOTHING, db_column='id', primary_key=True)
    groesse = models.IntegerField(blank=True, null=True)
    aufloesung = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitor'


class Notebook(models.Model):
    id = models.OneToOneField('Rechner', models.DO_NOTHING, db_column='id', primary_key=True)
    laptopname = models.TextField(blank=True, null=True)
    wlan = models.TextField(blank=True, null=True)  # This field type is a guess.
    bluetooth = models.TextField(blank=True, null=True)  # This field type is a guess.
    lte = models.TextField(blank=True, null=True)  # This field type is a guess.
    monitorgroesse = models.IntegerField(blank=True, null=True)
    tastatursprache = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notebook'


class Rechner(models.Model):
    id = models.OneToOneField(Hardware, models.DO_NOTHING, db_column='id', primary_key=True)
    internetname = models.TextField(blank=True, null=True)
    internetnummer = models.GenericIPAddressField(blank=True, null=True)
    junetmac = models.TextField(blank=True, null=True)  # This field type is a guess.
    betriebssystem = models.TextField(blank=True, null=True)
    backup = models.BooleanField(blank=True, null=True)
    backupzeitpunkt = models.TimeField(blank=True, null=True)
    backuptage = models.TextField(db_column='backupTage', blank=True, null=True)  # Field name made lowercase.
    backuppasswort = models.TextField(blank=True, null=True)
    remotedesktop = models.BooleanField(blank=True, null=True)
    lanonboard = models.TextField(blank=True, null=True)  # This field type is a guess.
    lanfiber = models.TextField(blank=True, null=True)  # This field type is a guess.
    teamviewerid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rechner'


class Software(models.Model):
    id = models.OneToOneField(Asset, models.DO_NOTHING, db_column='id', primary_key=True)
    name = models.TextField(blank=True, null=True)
    lizenz = models.TextField(blank=True, null=True)
    version = models.TextField(blank=True, null=True)
    ablaufdatum = models.DateField(blank=True, null=True)
    support = models.DateField(blank=True, null=True)
    zusatztool = models.TextField(blank=True, null=True)
    rechnerid = models.ForeignKey(Rechner, models.DO_NOTHING, db_column='rechnerid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'software'


class Ssd(models.Model):
    id = models.OneToOneField(Komponente, models.DO_NOTHING, db_column='id', primary_key=True)
    groesse = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssd'


class Zubehoer(models.Model):
    id = models.OneToOneField(Asset, models.DO_NOTHING, db_column='id', primary_key=True)
    zubehoertyp = models.IntegerField(blank=True, null=True)
    bezeichnung = models.TextField(blank=True, null=True)
    hardwareid = models.ForeignKey(Hardware, models.DO_NOTHING, db_column='hardwareid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zubehoer'


class Zusatzgeraet(models.Model):
    id = models.OneToOneField(Hardware, models.DO_NOTHING, db_column='id', primary_key=True)
    zusatzgeraetetyp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zusatzgeraet'
