from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def index(request,num):
    movieDet = Movie.objects.all()[:5]
    context = {'movie_list':movieDet}
    return render(request,'index.html',context)
    #return HttpResponse("Hello Index Page number  "+num)

def info(request,nam):
    '''movieDet = Movie.objects.get(title=nam)
    context = {'Movie':movieDet}'''
    movieObj = Movie.objects.get(title=nam)
    context = {'movie':movieObj}
    #return HttpResponse("Name is "+ nam)
    return render(request,'details.html',context)