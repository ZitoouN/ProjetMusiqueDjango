from django.shortcuts import render, HttpResponseRedirect
from .forms import MusiqueForm, AlbumForm
from . import models

def home(request):
    tmplate = "main.html"
    return render(request, 'musique/index.html')

def ajout(request):
    if request.method == "POST":
        form = MusiqueForm(request)
        return render(request,"musique/ajout.html",{"form" : form})
    else :
        form = MusiqueForm()
        return render(request, "musique/ajout.html", {"form" : form})

def ajout2(request):
    if request.method == "POST":
        form = AlbumForm(request)
        return render(request,"musique/ajout2.html",{"form" : form})
    else :
        form = AlbumForm()
        return render(request, "musique/ajout2.html", {"form" : form})

def traitement(request):
    mform = MusiqueForm(request.POST)
    if mform.is_valid():
        musique = mform.save()
        return HttpResponseRedirect('/musique/')
    else :
        return render(request,"musique/ajout.html", {"form" : mform})

def traitement2(request):
    aform = AlbumForm(request.POST)
    if aform.is_valid():
        album = aform.save()
        return HttpResponseRedirect('/musique/')
    else :
        return render(request,"musique/ajout2.html", {"form" : aform})


def affichage(request):
    liste = list(models.Musique.objects.all())
    return render(request, 'musique/affichage.html',{"liste" : liste})

def affichage2(request):
    listes = list(models.Album.objects.all())
    return render(request, 'musique/affichage2.html',{"listes" : listes})

def affiche(request, id):
    musique = models.Musique.objects.get(pk = id)
    return render(request,'musique/affiche.html',{"musique":musique})

def affiche2(request, id):
    album = models.Album.objects.get(pk = id)
    return render(request,'musique/affiche2.html',{"album":album})

def update(request, id):
    musique = models.Musique.objects.get(pk=id)
    form = MusiqueForm(musique.dico())
    return render(request, "musique/update.html", {"form":form, "id":id})

def updatetraitement(request, id):
    mform = MusiqueForm(request.POST)
    if mform.is_valid():
        musique = mform.save(commit = False)
        musique.id = id
        musique.save()
        return HttpResponseRedirect('/musique/affichage')
    else:
        return render(request, "musique/ajout.html", {"form": mform, "id":id})

def update2(request, id):
    album = models.Album.objects.get(pk=id)
    form = AlbumForm(album.dico2())
    return render(request, "musique/update2.html", {"form": form, "id": id})

def updatetraitement2(request, id):
    aform = AlbumForm(request.POST)
    if aform.is_valid():
        album = aform.save(commit = False)
        album.id = id
        album.save()
        return HttpResponseRedirect('/musique/affichage2')
    else:
        return render(request, "musique/ajout2.html", {"form": aform, "id":id})

def delete(request, id):
    musique = models.Musique.objects.get(pk=id)
    musique.delete()
    return HttpResponseRedirect('/musique/affichage')

def delete2(request, id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return HttpResponseRedirect('/musique/affichage2')