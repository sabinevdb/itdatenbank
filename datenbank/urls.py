from django.urls import path
from . import views
from .views import mitarbeiter
from .views import asset


urlpatterns = [
    path('', views.startseite, name='startseite'),
    path('mitarbeiter/', views.mitarbeiter), # http://127.0.0.1:8000/datenbank/mitarbeiter/
    path('mitarbeiterliste/', views.mitarbeiterliste, name='mitarbeiterliste'),
    path('mitarbeiter/<int:pk>/', views.mitarbeiter_detail, name='mitarbeiter_detail'),
    path('mitarbeiter/neu/', views.mitarbeiter_neu, name='mitarbeiter_neu'),
    path('mitarbeiter/<int:pk>/edit/', views.mitarbeiter_edit, name='mitarbeiter_edit'),
    path('assetliste/', views.assetliste, name='assetliste'),
    path('asset/<int:pk>/', views.asset_detail, name='asset_detail'),
    path('asset/neu/', views.asset_neu, name='asset_neu'),
    path('asset/<int:pk>/edit/', views.asset_edit, name='asset_edit'),
]
