from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('<slug:page_slug>/', views.page, name='page'),
    path('<slug:page_slug>/<slug:content_slug>/', views.content, name='content')
]
