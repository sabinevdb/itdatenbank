from django.urls import path
from . import views
from .views import mitarbeiter


urlpatterns = [
    path('mitarbeiter/', views.mitarbeiter), # http://127.0.0.1:8000/datenbank/mitarbeiter/
    path('mitarbeiterliste/', views.mitarbeiterliste),
    path('mitarbeiter/<int:pk>/', views.mitarbeiter_detail, name='mitarbeiter_detail'),
]
