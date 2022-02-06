from django.db import models
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import AN, Comment
from .models import Favourite
# from django.views import View
# Create your views here.
def ANIME(request):
    if request.method=="POST":
        search=request.POST.get("search")
        movie=AN.objects.filter(name__contains=search)
        return render(request,"anime/all.html",{ "animes":movie})

    anime=AN.objects.all()
    return render(request,"anime/all.html",{"animes":anime})

def watch(request , slug):
    a=AN.objects.get(slug=slug)
    a.viewsNum=a.viewsNum+1
    a.save()
    # v.save()
    if request.method=="POST":
        favanime=AN.objects.get(slug=slug) 
        favourites=Favourite.objects.get(user=request.user)
        if AN.objects.get(slug=slug) in Favourite.objects.filter(user=request.user).first().anime.all():
            favourites.anime.remove(favanime)
        else:
            favourites.anime.add(favanime)
    anime=AN.objects.get(slug=slug)
    return render(request,"anime/watch.html",{"anime":anime,'fav':Favourite.objects.filter(user=request.user).first().anime.all()})
def add(request):
    favanime=Favourite.objects.get(user=request.user).anime.all()
    if request.method=="POST":
        slug=request.POST.get("slug")
        ani=AN.objects.get(slug=slug)
        fav=Favourite.objects.get(user=request.user).anime.all()
        if ani in fav:
            Favourite.objects.get(user=request.user).anime.remove(ani)
    return render(request,"anime/favourite.html",{"animes":favanime})


def com(request , slug):
    if request.method=="POST":
        Content=request.POST.get("Content")
        user=request.user
        anime=AN.objects.get(slug=slug)
        comment= Comment.objects.create(content=Content , user=user , anime=anime)
        comment.save()
    anime=AN.objects.get(slug=slug)
    q=Comment.objects.filter(anime=anime) 
    return render(request , 'anime/addCom.html',{"commen":q})
