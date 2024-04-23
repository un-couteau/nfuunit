from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from db.models import NavMenu, Page, PageContent
from .serializers import NavMenuSerializer, PageSerializer, PageContentSerializer


class PageItemListList(generics.ListCreateAPIView):
    queryset = NavMenu.objects.all()
    serializer_class = NavMenuSerializer


class PageList(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageContentList(generics.ListCreateAPIView):
    queryset = PageContent.objects.all()
    serializer_class = PageContentSerializer
