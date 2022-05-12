from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# relative import of forms
from .models import Mitarbeiter
from .forms import MitarbeiterForm
from .models import Asset
from .forms import AssetForm
from django.shortcuts import redirect

# Create your views here.
def startseite(request):
    return render(request, 'datenbank/startseite.html', {})

def asset(request):
    return render(request, 'datenbank/asset.html', {})

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

def mitarbeiter_edit(request, pk):
    mitarbeiter = get_object_or_404(Mitarbeiter, pk=pk)
    if request.method == "POST":
        form = MitarbeiterForm(request.POST, instance=mitarbeiter)
        if form.is_valid():
            mitarbeiter = form.save(commit=False)
            mitarbeiter.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = MitarbeiterForm(instance=mitarbeiter)
    return render(request, 'datenbank/mitarbeiter_edit.html', {'form': form})

def assetliste(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Asset.objects.all()
    return render(request, "datenbank/assetliste.html", context)

def asset_detail(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    return render(request, 'datenbank/asset_detail.html', {'asset': asset})

def asset_neu(request):
    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            return redirect('asset_detail', pk=asset.pk)
    else:
        form = AssetForm()
    return render(request, 'datenbank/asset_edit.html', {'form': form})

def asset_edit(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == "POST":
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            return redirect('asset_detail', pk=asset.pk)
    else:
        form = AssetForm(instance=asset)
    return render(request, 'datenbank/asset_edit.html', {'form': form})
