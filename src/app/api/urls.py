from django.urls import path
from . import views

urlpatterns = [
    path('pageitemlist/', views.PageItemListList.as_view(), name='api_pageitemlist'),
    path('page/', views.PageList.as_view(), name='api_page'),
    path('pagecontent/', views.PageContentList.as_view(), name='api_pagecontent')
]
