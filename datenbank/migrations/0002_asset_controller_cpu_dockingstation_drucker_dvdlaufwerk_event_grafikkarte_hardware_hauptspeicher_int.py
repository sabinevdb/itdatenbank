# Generated by Django 3.2.12 on 2022-04-27 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datenbank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discriminator', models.CharField(blank=True, max_length=50, null=True)),
                ('bestellnummer', models.IntegerField(blank=True, null=True)),
                ('hersteller', models.TextField(blank=True, null=True)),
                ('haendler', models.TextField(blank=True, null=True)),
                ('raum', models.IntegerField(blank=True, null=True)),
                ('bemerkung', models.TextField(blank=True, null=True)),
                ('seriennummer', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'asset',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.IntegerField(blank=True, null=True)),
                ('datum', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.asset')),
                ('inventarnummer', models.IntegerField(blank=True, null=True, unique=True)),
                ('bezeichnung', models.TextField(blank=True, null=True)),
                ('schnittstellen', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hardware',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Komponente',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.asset')),
                ('modell', models.TextField(blank=True, null=True)),
                ('bus', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'komponente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.asset')),
                ('name', models.TextField(blank=True, null=True)),
                ('lizenz', models.TextField(blank=True, null=True)),
                ('version', models.TextField(blank=True, null=True)),
                ('ablaufdatum', models.DateField(blank=True, null=True)),
                ('support', models.DateField(blank=True, null=True)),
                ('zusatztool', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'software',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zubehoer',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.asset')),
                ('zubehoertyp', models.IntegerField(blank=True, null=True)),
                ('bezeichnung', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'zubehoer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Controller',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.komponente')),
            ],
            options={
                'db_table': 'controller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.komponente')),
                ('taktfrequenz', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cpu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dockingstation',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.hardware')),
                ('mac', models.TextField(blank=True, null=True)),
                ('junetip', models.GenericIPAddressField(blank=True, null=True)),
                ('junetname', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dockingstation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Drucker',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.hardware')),
                ('internetnummer', models.GenericIPAddressField(blank=True, null=True)),
                ('speicher', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'drucker',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dvdlaufwerk',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.komponente')),
                ('geschwindigkeit', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dvdlaufwerk',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Grafikkarte',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.komponente')),
                ('speicher', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'grafikkarte',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hauptspeicher',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.komponente')),
                ('groesse', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hauptspeicher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Internefestplatte',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.komponente')),
                ('groesse', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'internefestplatte',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.hardware')),
                ('groesse', models.IntegerField(blank=True, null=True)),
                ('aufloesung', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'monitor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rechner',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.hardware')),
                ('internetname', models.TextField(blank=True, null=True)),
                ('internetnummer', models.GenericIPAddressField(blank=True, null=True)),
                ('junetmac', models.TextField(blank=True, null=True)),
                ('betriebssystem', models.TextField(blank=True, null=True)),
                ('backup', models.BooleanField(blank=True, null=True)),
                ('backupzeitpunkt', models.TimeField(blank=True, null=True)),
                ('backuptage', models.TextField(blank=True, db_column='backupTage', null=True)),
                ('backuppasswort', models.TextField(blank=True, null=True)),
                ('remotedesktop', models.BooleanField(blank=True, null=True)),
                ('lanonboard', models.TextField(blank=True, null=True)),
                ('lanfiber', models.TextField(blank=True, null=True)),
                ('teamviewerid', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rechner',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ssd',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.komponente')),
                ('groesse', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ssd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zusatzgeraet',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.hardware')),
                ('zusatzgeraetetyp', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'zusatzgeraet',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='datenbank.rechner')),
                ('laptopname', models.TextField(blank=True, null=True)),
                ('wlan', models.TextField(blank=True, null=True)),
                ('bluetooth', models.TextField(blank=True, null=True)),
                ('lte', models.TextField(blank=True, null=True)),
                ('monitorgroesse', models.IntegerField(blank=True, null=True)),
                ('tastatursprache', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'notebook',
                'managed': False,
            },
        ),
    ]
