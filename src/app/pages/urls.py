from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("news/", views.news, name="news"),
    path("news/<int:pk>", views.news_item, name="news_item"),
    path('<slug:page_slug>/', views.page, name='page'),
    path('<slug:page_slug>/<slug:subpage_slug>/', views.subpage, name='subpage'),
    path('<slug:page_slug>/<slug:subpage_slug>/<slug:subsubpage_slug>/', views.subsubpage, name='subsubpage'),
    path('<slug:page_slug>/<slug:subpage_slug>/<slug:subsubpage_slug>/<slug:subsubsubpage_slug>/', views.subsubsubpage, name='subsubsubpage'),
]
