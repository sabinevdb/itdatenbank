from django.urls import path
from .views import mitarbeiter


urlpatterns = [
    path('mitarbeiter/', mitarbeiter), # http://127.0.0.1:8000/datenbank/mitarbeiter/
]
