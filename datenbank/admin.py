from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Asset
from .models import Cpu
from .models import Controller
from .models import Dockingstation
from .models import Drucker
from .models import Dvdlaufwerk
from .models import Event
from .models import Grafikkarte
from .models import Hardware
from .models import Hauptspeicher
from .models import Internefestplatte
from .models import Komponente
from .models import Mitarbeiter
from .models import Monitor
from .models import Notebook
from .models import Rechner
from .models import Software
from .models import Ssd
from .models import Zubehoer
from .models import Zusatzgeraet

admin.site.register(Asset)
admin.site.register(Cpu)
admin.site.register(Controller)
admin.site.register(Dockingstation)
admin.site.register(Drucker)
admin.site.register(Dvdlaufwerk)
admin.site.register(Event)
admin.site.register(Grafikkarte)
admin.site.register(Hardware)
admin.site.register(Hauptspeicher)
admin.site.register(Internefestplatte)
admin.site.register(Komponente)
admin.site.register(Mitarbeiter)
admin.site.register(Monitor)
admin.site.register(Notebook)
admin.site.register(Rechner)
admin.site.register(Software)
admin.site.register(Ssd)
admin.site.register(Zubehoer)
admin.site.register(Zusatzgeraet)
