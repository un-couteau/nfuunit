from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('university/', TemplateView.as_view(template_name='main/university.html'), name='university'),
    path('applicants/', TemplateView.as_view(template_name='main/applicants.html'), name='applicants'),
    path('students/', TemplateView.as_view(template_name='main/students.html'), name='students'),
    path('science/', TemplateView.as_view(template_name='main/science.html'), name='science'),
    path('<slug:page_slug>/', views.page, name='page'),
    path('<slug:page_slug>/<slug:subpage_slug>', views.subpage, name='subpage'),
]
