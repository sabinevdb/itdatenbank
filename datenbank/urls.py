from django.urls import path
from . import views
from .views import mitarbeiter


urlpatterns = [
    path('', views.startseite, name='startseite'),
    path('mitarbeiter/', views.mitarbeiter), # http://127.0.0.1:8000/datenbank/mitarbeiter/
    path('mitarbeiterliste/', views.mitarbeiterliste),
    path('mitarbeiter/<int:pk>/', views.mitarbeiter_detail, name='mitarbeiter_detail'),
    path('mitarbeiter/neu/', views.mitarbeiter_neu, name='mitarbeiter_neu'),
]
