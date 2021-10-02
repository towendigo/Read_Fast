from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from .serializers import BaseAuthorSerializer, AuthorSerializer

from readfast.model_loader import Multi_Loader
from .models import LanguageSet

LanguageDict = LanguageSet()
LanguageObjectSet = LanguageSet().values()
LanguageObjectSet = Multi_Loader("author", LanguageObjectSet)

def GetAll(request, lan='en'):
    if request.method == 'GET':
        if lan not in LanguageDict.keys():
            lan = 'en'
        object_model = LanguageObjectSet[LanguageDict[lan]] 
        books = object_model.objects.all()
        serializer = AuthorSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)

def GetById(request, author_id, lan='en'):
    if request.method == 'GET':
        if lan not in LanguageDict.keys():
            lan = 'en'
        
        object_model = LanguageObjectSet[LanguageDict[lan]] 
        book = object_model.objects.get(author=author_id)
        serializer = AuthorSerializer(book)
        return JsonResponse(serializer.data, safe=False)

def GetByName(request, author_name, lan='en'):
    if request.method == 'GET':
        if lan not in LanguageDict.keys():
            lan = 'en'

        object_model = LanguageObjectSet[LanguageDict[lan]] 
        books = object_model.objects.filter(author__author_name__icontains=author_name)
        serializer = AuthorSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)