from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# relative import of forms
from .models import Mitarbeiter
from .forms import MitarbeiterForm
from django.shortcuts import redirect

# Create your views here.
def mitarbeiter(request):
    return render(request, 'datenbank/mitarbeiter.html', {})

def mitarbeiterliste(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Mitarbeiter.objects.all()
    return render(request, "datenbank/mitarbeiterliste.html", context)

def mitarbeiter_detail(request, pk):
    mitarbeiter = get_object_or_404(Mitarbeiter, pk=pk)
    return render(request, 'datenbank/mitarbeiter_detail.html', {'mitarbeiter': mitarbeiter})

def startseite(request):
    return render(request, 'datenbank/startseite.html', {})

def mitarbeiter_neu(request):
    if request.method == "POST":
        form = MitarbeiterForm(request.POST)
        if form.is_valid():
            mitarbeiter = form.save(commit=False)
            mitarbeiter.save()
            return redirect('mitarbeiter_detail', pk=mitarbeiter.pk)
    else:
        form = MitarbeiterForm()
    return render(request, 'datenbank/mitarbeiter_edit.html', {'form': form})
