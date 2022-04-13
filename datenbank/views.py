from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mitarbeiter(request):
    return render(request, 'datenbank/mitarbeiter.html', {})
