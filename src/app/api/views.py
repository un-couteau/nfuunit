from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from db.models import PageItemList, Page, PageContent
from .serializers import PageItemListSerializer, PageSerializer, PageContentSerializer


class PageItemListList(generics.ListCreateAPIView):
    queryset = PageItemList.objects.all()
    serializer_class = PageItemListSerializer


class PageList(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageContentList(generics.ListCreateAPIView):
    queryset = PageContent.objects.all()
    serializer_class = PageContentSerializer
